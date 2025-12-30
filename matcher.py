"""
Enterprise-Grade ATS Matcher - COMPLETELY FIXED
Critical Fixes:
1. OR group detection now captures full skill names correctly
2. Checks if OR group skills are already matched before marking as missing
3. Data visualization tools (Tableau/Power BI) now satisfy "data visualization" requirement
4. Better skill normalization and grouping
"""
import spacy
from sentence_transformers import SentenceTransformer, util
from config import STOP_WORDS, SKILL_SYNONYMS, EXPLICIT_NON_SKILLS
import re
from collections import Counter
import numpy as np

# Load NLP Models
try:
    nlp = spacy.load("en_core_web_sm")
except:
    print("Downloading spacy model...")
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

model = SentenceTransformer('all-MiniLM-L6-v2')

class EnterpriseATSMatcher:
    """
    Multi-layer matching system with OR logic support
    """
    
    def __init__(self):
        self.skill_categories = self._categorize_skills()
        # COMPREHENSIVE: Define which tools/skills imply other capabilities
        # Format: 'specific_tool': ['broader_capability1', 'broader_capability2']
        self.skill_implies = {
            # ===== DATA VISUALIZATION & BI =====
            'tableau': ['data visualization', 'business intelligence', 'data analytics', 'dashboarding'],
            'power bi': ['data visualization', 'business intelligence', 'data analytics', 'dashboarding'],
            'qlikview': ['data visualization', 'business intelligence', 'data analytics'],
            'looker': ['data visualization', 'business intelligence', 'data analytics'],
            'metabase': ['data visualization', 'business intelligence'],
            'superset': ['data visualization', 'business intelligence'],
            'matplotlib': ['data visualization', 'data analytics'],
            'seaborn': ['data visualization', 'data analytics'],
            'plotly': ['data visualization', 'data analytics'],
            'bokeh': ['data visualization', 'data analytics'],
            'altair': ['data visualization'],
            'd3.js': ['data visualization', 'javascript'],
            
            # ===== DATA SCIENCE & ANALYTICS =====
            'pandas': ['data analytics', 'data science', 'python'],
            'numpy': ['data analytics', 'data science', 'python'],
            'scipy': ['data analytics', 'data science', 'python'],
            'r programming': ['data analytics', 'data science', 'statistical analysis'],
            'spss': ['statistical analysis', 'data analytics'],
            'stata': ['statistical analysis', 'data analytics'],
            'sas': ['statistical analysis', 'data analytics'],
            
            # ===== MACHINE LEARNING & AI =====
            'scikit-learn': ['machine learning', 'data science', 'python'],
            'tensorflow': ['machine learning', 'deep learning', 'artificial intelligence', 'python'],
            'pytorch': ['machine learning', 'deep learning', 'artificial intelligence', 'python'],
            'keras': ['machine learning', 'deep learning', 'artificial intelligence', 'python'],
            'xgboost': ['machine learning', 'data science'],
            'lightgbm': ['machine learning', 'data science'],
            'catboost': ['machine learning', 'data science'],
            'fastai': ['machine learning', 'deep learning', 'python'],
            'huggingface transformers': ['natural language processing', 'machine learning', 'artificial intelligence'],
            'spacy': ['natural language processing', 'python'],
            'nltk': ['natural language processing', 'python'],
            'opencv': ['computer vision', 'python', 'image processing'],
            
            # ===== WEB DEVELOPMENT - FRONTEND =====
            'react': ['javascript', 'web development', 'front end', 'ui development'],
            'angular': ['javascript', 'typescript', 'web development', 'front end'],
            'vue': ['javascript', 'web development', 'front end'],
            'svelte': ['javascript', 'web development', 'front end'],
            'next.js': ['react', 'javascript', 'web development', 'front end'],
            'nuxt.js': ['vue', 'javascript', 'web development', 'front end'],
            'gatsby': ['react', 'javascript', 'web development'],
            'jquery': ['javascript', 'web development'],
            'bootstrap': ['css', 'web development', 'responsive design'],
            'tailwind css': ['css', 'web development', 'responsive design'],
            'material ui': ['react', 'ui design', 'web development'],
            'ant design': ['react', 'ui design', 'web development'],
            'sass': ['css', 'web development'],
            'less': ['css', 'web development'],
            
            # ===== WEB DEVELOPMENT - BACKEND =====
            'node.js': ['javascript', 'web development', 'back end', 'server side'],
            'express.js': ['node.js', 'javascript', 'web development', 'back end'],
            'nest.js': ['node.js', 'typescript', 'web development', 'back end'],
            'django': ['python', 'web development', 'back end'],
            'flask': ['python', 'web development', 'back end'],
            'fastapi': ['python', 'web development', 'back end', 'api development'],
            'spring framework': ['java', 'web development', 'back end'],
            'spring boot': ['java', 'spring framework', 'web development', 'back end'],
            'ruby on rails': ['ruby', 'web development', 'back end'],
            'laravel': ['php', 'web development', 'back end'],
            'symfony': ['php', 'web development', 'back end'],
            'asp.net': ['c#', 'web development', 'back end'],
            'asp.net core': ['c#', 'web development', 'back end'],
            
            # ===== MOBILE DEVELOPMENT =====
            'react native': ['javascript', 'react', 'mobile development', 'cross platform'],
            'flutter': ['dart', 'mobile development', 'cross platform'],
            'android development': ['java', 'kotlin', 'mobile development'],
            'ios development': ['swift', 'objective-c', 'mobile development'],
            'swiftui': ['swift', 'ios development', 'ui design'],
            'jetpack compose': ['kotlin', 'android development', 'ui design'],
            'ionic': ['javascript', 'mobile development', 'cross platform'],
            'xamarin': ['c#', 'mobile development', 'cross platform'],
            
            # ===== DATABASES =====
            'mysql': ['sql', 'database management', 'relational database'],
            'postgresql': ['sql', 'database management', 'relational database'],
            'oracle database': ['sql', 'database management', 'relational database'],
            'sql server': ['sql', 'database management', 'relational database'],
            'mongodb': ['nosql', 'database management'],
            'redis': ['nosql', 'database management', 'caching'],
            'elasticsearch': ['nosql', 'database management', 'search'],
            'cassandra': ['nosql', 'database management', 'big data'],
            'dynamodb': ['nosql', 'database management', 'amazon web services'],
            'firebase': ['nosql', 'database management', 'back end'],
            'neo4j': ['nosql', 'graph database', 'database management'],
            
            # ===== CLOUD PLATFORMS =====
            'amazon ec2': ['amazon web services', 'cloud computing', 'infrastructure'],
            'amazon s3': ['amazon web services', 'cloud computing', 'storage'],
            'aws lambda': ['amazon web services', 'cloud computing', 'serverless architecture'],
            'amazon rds': ['amazon web services', 'cloud computing', 'database management'],
            'amazon eks': ['amazon web services', 'kubernetes', 'cloud computing'],
            'sagemaker': ['amazon web services', 'machine learning', 'cloud computing'],
            'redshift': ['amazon web services', 'data warehousing', 'cloud computing'],
            'bigquery': ['google cloud platform', 'data warehousing', 'sql', 'cloud computing'],
            'google kubernetes engine': ['google cloud platform', 'kubernetes', 'cloud computing'],
            'vertex ai': ['google cloud platform', 'machine learning', 'cloud computing'],
            'azure functions': ['microsoft azure', 'cloud computing', 'serverless architecture'],
            'azure kubernetes service': ['microsoft azure', 'kubernetes', 'cloud computing'],
            'azure machine learning': ['microsoft azure', 'machine learning', 'cloud computing'],
            'cosmos db': ['microsoft azure', 'nosql', 'database management'],
            
            # ===== DEVOPS & CI/CD =====
            'docker': ['containerization', 'devops', 'cloud computing'],
            'kubernetes': ['containerization', 'devops', 'cloud computing', 'orchestration'],
            'jenkins': ['ci/cd', 'devops', 'automation'],
            'gitlab ci': ['ci/cd', 'devops', 'automation'],
            'github actions': ['ci/cd', 'devops', 'automation'],
            'circle ci': ['ci/cd', 'devops', 'automation'],
            'terraform': ['infrastructure as code', 'devops', 'cloud computing'],
            'ansible': ['infrastructure as code', 'devops', 'automation', 'configuration management'],
            'puppet': ['infrastructure as code', 'devops', 'configuration management'],
            'chef': ['infrastructure as code', 'devops', 'configuration management'],
            'helm': ['kubernetes', 'devops', 'package management'],
            'prometheus': ['monitoring', 'devops', 'observability'],
            'grafana': ['monitoring', 'devops', 'data visualization', 'observability'],
            'datadog': ['monitoring', 'devops', 'observability'],
            'splunk': ['monitoring', 'log management', 'security'],
            
            # ===== BIG DATA =====
            'hadoop': ['big data', 'data engineering', 'distributed computing'],
            'apache spark': ['big data', 'data engineering', 'distributed computing'],
            'kafka': ['big data', 'data engineering', 'message queue', 'streaming'],
            'airflow': ['data engineering', 'workflow automation', 'etl'],
            'apache flink': ['big data', 'data engineering', 'streaming'],
            'snowflake': ['data warehousing', 'cloud computing', 'sql'],
            'databricks': ['big data', 'data engineering', 'apache spark', 'machine learning'],
            'dbt': ['data engineering', 'data warehousing', 'sql', 'etl'],
            
            # ===== CYBERSECURITY =====
            'metasploit': ['penetration testing', 'cybersecurity', 'ethical hacking'],
            'burp suite': ['penetration testing', 'cybersecurity', 'web security'],
            'wireshark': ['network security', 'cybersecurity', 'network analysis'],
            'nmap': ['network security', 'cybersecurity', 'penetration testing'],
            'kali linux': ['penetration testing', 'cybersecurity', 'ethical hacking'],
            'splunk': ['siem', 'cybersecurity', 'log management'],
            
            # ===== API & INTEGRATION =====
            'rest api': ['api development', 'web services', 'back end'],
            'graphql': ['api development', 'web services', 'back end'],
            'grpc': ['api development', 'web services', 'back end'],
            'soap': ['api development', 'web services'],
            'rabbitmq': ['message queue', 'back end', 'integration'],
            'activemq': ['message queue', 'back end', 'integration'],
            'websockets': ['real-time communication', 'web development'],
            
            # ===== DESIGN & CREATIVE =====
            'adobe photoshop': ['graphic design', 'visual design', 'image editing'],
            'adobe illustrator': ['graphic design', 'visual design', 'vector graphics'],
            'adobe indesign': ['graphic design', 'layout design', 'desktop publishing'],
            'figma': ['ui design', 'ux design', 'web design', 'collaboration'],
            'sketch': ['ui design', 'ux design', 'web design'],
            'adobe xd': ['ui design', 'ux design', 'web design', 'prototyping'],
            'invision': ['ui design', 'ux design', 'prototyping'],
            'adobe after effects': ['motion graphics', 'video editing', 'animation'],
            'adobe premiere': ['video editing', 'video production'],
            'final cut pro': ['video editing', 'video production'],
            'blender': ['3d modeling', '3d animation', 'visual effects'],
            'maya': ['3d modeling', '3d animation', 'visual effects'],
            'cinema 4d': ['3d modeling', 'motion graphics', 'visual effects'],
            
            # ===== BUSINESS & ERP =====
            'sap': ['erp', 'enterprise resource planning', 'business management'],
            'oracle erp': ['erp', 'enterprise resource planning', 'business management'],
            'netsuite': ['erp', 'enterprise resource planning', 'cloud computing'],
            'salesforce': ['crm', 'customer relationship management', 'sales'],
            'hubspot': ['crm', 'marketing automation', 'sales'],
            'quickbooks': ['accounting', 'bookkeeping', 'finance'],
            'xero': ['accounting', 'bookkeeping', 'finance'],
            
            # ===== PROJECT MANAGEMENT =====
            'jira': ['project management', 'agile methodology', 'issue tracking'],
            'confluence': ['project management', 'documentation', 'collaboration'],
            'trello': ['project management', 'kanban', 'task management'],
            'asana': ['project management', 'task management', 'collaboration'],
            'monday.com': ['project management', 'task management', 'collaboration'],
            
            # ===== MARKETING =====
            'google analytics': ['digital marketing', 'web analytics', 'data analytics'],
            'google tag manager': ['digital marketing', 'web analytics', 'tag management'],
            'google ads': ['digital marketing', 'ppc', 'sem', 'advertising'],
            'facebook ads': ['digital marketing', 'social media marketing', 'advertising'],
            'mailchimp': ['email marketing', 'marketing automation'],
            'hubspot': ['marketing automation', 'crm', 'inbound marketing'],
            'marketo': ['marketing automation', 'lead generation'],
            
            # ===== HEALTHCARE =====
            'epic': ['electronic health records', 'healthcare', 'medical software'],
            'cerner': ['electronic health records', 'healthcare', 'medical software'],
            
            # ===== ENGINEERING & CAD =====
            'autocad': ['cad', 'computer aided design', 'drafting', 'engineering'],
            'solidworks': ['cad', 'computer aided design', '3d modeling', 'mechanical engineering'],
            'catia': ['cad', 'computer aided design', '3d modeling', 'engineering'],
            'fusion 360': ['cad', 'computer aided design', '3d modeling'],
            'inventor': ['cad', 'computer aided design', '3d modeling'],
            'creo': ['cad', 'computer aided design', '3d modeling'],
            'ansys': ['fea', 'simulation', 'engineering analysis'],
            'comsol': ['simulation', 'engineering analysis', 'multiphysics'],
            
            # ===== TESTING =====
            'selenium': ['test automation', 'web testing', 'quality assurance'],
            'cypress': ['test automation', 'web testing', 'javascript'],
            'jest': ['test automation', 'javascript', 'unit testing'],
            'pytest': ['test automation', 'python', 'unit testing'],
            'junit': ['test automation', 'java', 'unit testing'],
            'postman': ['api testing', 'rest api', 'quality assurance'],
            
            # ===== VERSION CONTROL =====
            'git': ['version control', 'collaboration', 'software development'],
            'github': ['version control', 'git', 'collaboration', 'devops'],
            'gitlab': ['version control', 'git', 'collaboration', 'devops', 'ci/cd'],
            'bitbucket': ['version control', 'git', 'collaboration'],
        }
        
    def _categorize_skills(self):
        """Group skills by category for weighted scoring"""
        categories = {
            'technical': ['python', 'java', 'javascript', 'react', 'node', 'sql', 'aws', 
                         'docker', 'kubernetes', 'machine learning', 'deep learning', 
                         'tensorflow', 'pytorch', 'artificial intelligence', 'pandas', 
                         'numpy', 'tableau', 'power bi', 'data visualization'],
            'management': ['project management', 'leadership', 'agile', 'scrum', 'team management',
                          'stakeholder management', 'strategic planning'],
            'soft_skills': ['communication skills', 'problem solving', 'teamwork', 'collaboration',
                           'critical thinking', 'adaptability'],
            'domain': ['finance', 'healthcare', 'marketing', 'sales', 'accounting', 'legal',
                      'data analytics', 'data science', 'business intelligence']
        }
        return categories
    
    def extract_skills_advanced(self, text, context="resume"):
        """
        FIXED: Advanced skill extraction with strict filtering
        """
        text_lower = text.lower()
        skills = set()
        
        # Get all valid skill values
        all_skill_values = set(SKILL_SYNONYMS.values())
        
        # Method 1: Direct matching with word boundaries
        for skill in all_skill_values:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                if skill not in STOP_WORDS and skill not in EXPLICIT_NON_SKILLS:
                    skills.add(skill)
        
        # Method 2: Match abbreviations/aliases
        sorted_skills = sorted(SKILL_SYNONYMS.items(), key=lambda x: len(x[0]), reverse=True)
        matched_positions = set()
        
        for abbr, full_skill in sorted_skills:
            pattern = r'\b' + re.escape(abbr) + r'\b'
            matches = re.finditer(pattern, text_lower)
            
            for match in matches:
                start, end = match.span()
                if not any(start < pos[1] and end > pos[0] for pos in matched_positions):
                    if full_skill not in STOP_WORDS and full_skill not in EXPLICIT_NON_SKILLS:
                        skills.add(full_skill)
                        matched_positions.add((start, end))
        
        # Method 3: Special compound terms
        special_patterns = [
            (r'\bc\+\+\b', 'c++'),
            (r'\bc#\b', 'c#'),
            (r'\bnode\.?js\b', 'node.js'),
            (r'\breact\.?js\b', 'react'),
        ]
        
        for pattern, skill in special_patterns:
            if re.search(pattern, text_lower):
                skills.add(skill)
        
        # FINAL CLEANUP
        skills_clean = set()
        for skill in skills:
            if skill in EXPLICIT_NON_SKILLS or skill in STOP_WORDS:
                continue
            if len(skill) < 2 or skill.isdigit():
                continue
            words = skill.split()
            if len(words) > 1 and all(w in STOP_WORDS for w in words):
                continue
            
            skills_clean.add(skill)
        
        return skills_clean
    
    def calculate_experience_weight(self, resume_text, skill):
        """Calculate years of experience with a skill"""
        skill_pattern = re.escape(skill)
        text_lower = resume_text.lower()
        
        patterns = [
            rf'(\d+)\s*(?:\+)?\s*years?\s*(?:of\s*)?(?:experience\s*)?(?:with\s*)?(?:in\s*)?{skill_pattern}',
            rf'{skill_pattern}\s*(?:for\s*)?(\d+)\s*(?:\+)?\s*years?',
            rf'{skill_pattern}\s*\((\d+)\s*(?:\+)?\s*years?\)',
            rf'{skill_pattern}.*?(?:for|over)\s+(\d+)\s*(?:\+)?\s*years?',
            rf'(\d+)\s*(?:\+)?\s*years?.*?{skill_pattern}',
        ]
        
        max_years = 0
        for pattern in patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            if matches:
                for match in matches:
                    try:
                        year_val = int(match) if isinstance(match, str) else int(match[0] if isinstance(match, tuple) else match)
                        max_years = max(max_years, year_val)
                    except (ValueError, IndexError):
                        continue
        
        # Context-based detection
        if max_years == 0:
            job_pattern = rf'(?:at|with)\s+[\w\s&]+(?:for|over)\s+(\d+)\s*(?:\+)?\s*years?'
            job_matches = re.finditer(job_pattern, text_lower)
            
            for match in job_matches:
                try:
                    year_val = int(match.group(1))
                    pos = match.start()
                    context_start = max(0, pos - 300)
                    context_end = min(len(text_lower), pos + 300)
                    context = text_lower[context_start:context_end]
                    
                    if skill in context or any(word in context for word in skill.split()):
                        max_years = max(max_years, year_val)
                except (ValueError, AttributeError):
                    continue
        
        return min(max_years, 15)
    
    def semantic_similarity_scored(self, jd_text, resume_text):
        """Multi-level semantic matching"""
        jd_embedding = model.encode(jd_text, convert_to_tensor=True)
        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        overall_similarity = util.pytorch_cos_sim(jd_embedding, resume_embedding).item()
        
        sections = self._extract_sections(resume_text)
        section_scores = {}
        
        if sections:
            for section_name, section_text in sections.items():
                if len(section_text) > 20:
                    section_embedding = model.encode(section_text, convert_to_tensor=True)
                    section_sim = util.pytorch_cos_sim(jd_embedding, section_embedding).item()
                    section_scores[section_name] = section_sim * 100
        
        return {
            'overall': overall_similarity * 100,
            'sections': section_scores
        }
    
    def _extract_sections(self, resume_text):
        """Extract resume sections"""
        sections = {}
        section_patterns = {
            'experience': r'(?:work\s+)?experience|employment\s+history|professional\s+experience',
            'education': r'education|academic\s+background|qualifications',
            'skills': r'(?:technical\s+)?skills|competencies|expertise',
            'projects': r'projects|portfolio',
        }
        
        lines = resume_text.split('\n')
        current_section = None
        
        for line in lines:
            line_lower = line.lower().strip()
            section_found = False
            
            for section_name, pattern in section_patterns.items():
                if re.search(pattern, line_lower) and len(line_lower) < 50:
                    current_section = section_name
                    sections[section_name] = ""
                    section_found = True
                    break
            
            if not section_found and current_section:
                sections[current_section] += line + "\n"
        
        return sections
    
    def _detect_skill_groups(self, jd_text):
        """
        IMPROVED: Detect OR groups like "Tableau or Power BI"
        Now with better pattern matching for all variations
        """
        or_groups = {}
        group_id = 0
        
        text_lower = jd_text.lower()
        
        # Multiple patterns to catch different variations
        or_patterns = [
            # Pattern 1: "skill1 or skill2" with word boundaries
            r'\b([\w\s.+-]+?)\s+or\s+([\w\s.+-]+?)(?=\s*[.,;:\n]|\s+(?:and|with|for|to|in)\s|\s*$)',
            
            # Pattern 2: "skill1/skill2"
            r'\b([\w\s.+-]+?)\s*/\s*([\w\s.+-]+?)(?=\s*[.,;:\n]|\s+(?:and|with|for|to|in)\s|\s*$)',
            
            # Pattern 3: Simple "word or word" 
            r'\b(\w+(?:\s+\w+)?)\s+or\s+(\w+(?:\s+\w+)?)\b',
        ]
        
        for pattern in or_patterns:
            matches = re.finditer(pattern, text_lower)
            for match in matches:
                try:
                    skill1_raw = match.group(1).strip()
                    skill2_raw = match.group(2).strip()
                    
                    # Skip if too long (likely sentence fragments)
                    if len(skill1_raw) > 50 or len(skill2_raw) > 50:
                        continue
                    
                    # Clean up: remove leading/trailing stop words and punctuation
                    skill1_clean = self._clean_skill_phrase(skill1_raw).strip('.,;:')
                    skill2_clean = self._clean_skill_phrase(skill2_raw).strip('.,;:')
                    
                    # Skip if empty after cleaning
                    if not skill1_clean or not skill2_clean:
                        continue
                    
                    # Skip common false positives
                    if skill1_clean in ['one', 'two', 'more', 'less', 'other', 'another']:
                        continue
                    
                    # Normalize to our skill database
                    skill1_norm = SKILL_SYNONYMS.get(skill1_clean, skill1_clean)
                    skill2_norm = SKILL_SYNONYMS.get(skill2_clean, skill2_clean)
                    
                    # Check if these are real skills
                    all_skills = set(SKILL_SYNONYMS.values())
                    
                    # Create group if at least one is a valid skill
                    if skill1_norm in all_skills or skill2_norm in all_skills:
                        # Avoid duplicates
                        group_key = tuple(sorted([skill1_norm, skill2_norm]))
                        if group_key not in [tuple(sorted(v)) for v in or_groups.values()]:
                            or_groups[f"group_{group_id}"] = [skill1_norm, skill2_norm]
                            group_id += 1
                except (IndexError, AttributeError):
                    continue
        
        return or_groups
    
    def _clean_skill_phrase(self, phrase):
        """Remove stop words and punctuation from beginning/end of skill phrase"""
        if not phrase:
            return ""
        
        # Remove common punctuation first
        phrase = phrase.strip('.,;:!?()[]{}')
        
        words = phrase.split()
        
        # Remove leading stop words
        while words and (words[0] in STOP_WORDS or words[0] in ['using', 'with', 'by', 'via', 'like']):
            words.pop(0)
        
        # Remove trailing stop words
        while words and (words[-1] in STOP_WORDS or words[-1] in ['and', 'or']):
            words.pop()
        
        cleaned = ' '.join(words)
        
        # Remove any remaining punctuation
        cleaned = cleaned.strip('.,;:!?()[]{}')
        
        return cleaned
    
    def _expand_skills_with_implications(self, cv_skills):
        """
        CRITICAL FIX: Expand CV skills to include implied skills
        E.g., if CV has "Tableau", add "data visualization"
        """
        expanded_skills = set(cv_skills)
        
        for skill in cv_skills:
            if skill in self.skill_implies:
                implied = self.skill_implies[skill]
                expanded_skills.update(implied)
        
        return expanded_skills
    
    def calculate_skill_priority(self, jd_text):
        """
        BALANCED: Determine must-have vs nice-to-have with intelligent categorization
        """
        must_have = set()
        nice_to_have = set()
        or_groups = self._detect_skill_groups(jd_text)
        
        all_skills = self.extract_skills_advanced(jd_text, context="jd")
        
        # Stronger must-have keywords
        must_keywords = ['must have', 'required', 'mandatory', 'essential', 'must know']
        nice_keywords = ['nice to have', 'preferred', 'desired', 'plus', 'bonus', 'optional', 'advantage']
        
        sentences = re.split(r'[.!\n]+', jd_text.lower())
        
        for sentence in sentences:
            is_must = any(keyword in sentence for keyword in must_keywords)
            is_nice = any(keyword in sentence for keyword in nice_keywords)
            
            sentence_skills = self.extract_skills_advanced(sentence, context="jd")
            
            if is_nice:
                nice_to_have.update(sentence_skills & all_skills)
            elif is_must:
                must_have.update(sentence_skills & all_skills)
            else:
                # BALANCED: Default to must-have for technical skills, nice-to-have for soft skills
                for skill in sentence_skills & all_skills:
                    # Check if it's a soft skill
                    if skill in ['communication skills', 'teamwork', 'collaboration', 
                                'leadership', 'problem solving', 'critical thinking',
                                'adaptability', 'creativity', 'time management']:
                        nice_to_have.add(skill)
                    else:
                        must_have.add(skill)
        
        # Remove overlap
        must_have = must_have - nice_to_have
        
        # If nothing categorized, treat core technical skills as must-have
        if not must_have and not nice_to_have:
            for skill in all_skills:
                if skill in ['communication skills', 'teamwork', 'leadership', 'collaboration']:
                    nice_to_have.add(skill)
                else:
                    must_have.add(skill)
        
        # CRITICAL: Remove OR group skills from must_have
        # They'll be evaluated as part of their OR group only
        all_or_group_skills = set()
        for group_skills in or_groups.values():
            all_or_group_skills.update(group_skills)
        
        must_have = must_have - all_or_group_skills
        nice_to_have = nice_to_have - all_or_group_skills
        
        return {
            'must_have': must_have,
            'nice_to_have': nice_to_have,
            'or_groups': or_groups
        }
    
    def _calculate_skill_similarity(self, required_skill, candidate_skills):
        """
        Calculate similarity between a required skill and candidate's skills
        Returns 0.0 to 1.0 (partial credit for related skills)
        """
        # Exact match
        if required_skill in candidate_skills:
            return 1.0
        
        # CRITICAL: Check if candidate has equivalent tool in same category
        equivalent_tools = {
            'tableau': ['power bi', 'qlikview', 'looker'],
            'power bi': ['tableau', 'qlikview', 'looker'],
            'qlikview': ['tableau', 'power bi', 'looker'],
            'react': ['angular', 'vue', 'svelte'],
            'angular': ['react', 'vue', 'svelte'],
            'vue': ['react', 'angular', 'svelte'],
            'mysql': ['postgresql', 'sql server', 'oracle database'],
            'postgresql': ['mysql', 'sql server', 'oracle database'],
            'mongodb': ['dynamodb', 'couchdb', 'cassandra'],
            'docker': ['podman', 'containerd'],
            'jenkins': ['gitlab ci', 'github actions', 'circle ci'],
            'terraform': ['cloudformation', 'pulumi'],
            'aws': ['azure', 'google cloud platform'],
            'amazon web services': ['microsoft azure', 'google cloud platform'],
            'microsoft azure': ['amazon web services', 'google cloud platform'],
        }
        
        # If candidate has equivalent tool, give HIGH partial credit (0.95)
        if required_skill in equivalent_tools:
            for equiv in equivalent_tools[required_skill]:
                if equiv in candidate_skills:
                    return 0.95  # Almost full credit for equivalent tools
        
        # Check for related skills (partial credit)
        related_skills = {
            'python': ['django', 'flask', 'fastapi', 'pandas', 'numpy'],
            'javascript': ['react', 'angular', 'vue', 'node.js', 'typescript'],
            'web development': ['react', 'angular', 'vue', 'html', 'css', 'node.js'],
            'database management': ['mysql', 'postgresql', 'mongodb', 'sql'],
            'cloud computing': ['amazon web services', 'microsoft azure', 'google cloud platform'],
            'data science': ['machine learning', 'data analytics', 'pandas', 'numpy'],
            'machine learning': ['tensorflow', 'pytorch', 'scikit-learn'],
        }
        
        # If candidate has related skills, give moderate partial credit
        if required_skill in related_skills:
            matching_related = set(related_skills[required_skill]) & candidate_skills
            if matching_related:
                return 0.7  # 70% credit for related skills
        
        # Check reverse (candidate has broader skill)
        for broad_skill, specific_skills in related_skills.items():
            if required_skill in specific_skills and broad_skill in candidate_skills:
                return 0.8  # 80% credit for having broader skill
        
        return 0.0
    
    def analyze_resume(self, job_description, resume_text):
        """
        BALANCED: Fair matching with partial credit for related skills
        """
        # Extract skills
        jd_skills_all = self.extract_skills_advanced(job_description, context="jd")
        cv_skills_raw = self.extract_skills_advanced(resume_text, context="resume")
        
        # Expand CV skills with implications
        cv_skills_all = self._expand_skills_with_implications(cv_skills_raw)
        
        skill_priority = self.calculate_skill_priority(job_description)
        must_have = skill_priority['must_have']
        nice_to_have = skill_priority['nice_to_have']
        or_groups = skill_priority['or_groups']
        
        # Process matching with partial credit
        must_have_matched = set()
        must_have_missing = set()
        partial_matches = {}  # Track partial credit
        
        # Step 1: Process OR groups
        for group_id, group_skills in or_groups.items():
            matched_from_group = [s for s in group_skills if s in cv_skills_all]
            
            if matched_from_group:
                must_have_matched.update(matched_from_group)
            else:
                # Check for partial matches in OR group
                best_similarity = 0.0
                for skill in group_skills:
                    similarity = self._calculate_skill_similarity(skill, cv_skills_all)
                    best_similarity = max(best_similarity, similarity)
                
                if best_similarity > 0.0:
                    partial_matches[f"({' or '.join(group_skills)})"] = best_similarity
                else:
                    must_have_missing.add(f"({' or '.join(group_skills)})")
        
        # Step 2: Process individual skills with partial credit
        for skill in must_have:
            if skill in cv_skills_all:
                must_have_matched.add(skill)
            else:
                # Check for partial match
                similarity = self._calculate_skill_similarity(skill, cv_skills_all)
                if similarity > 0.0:
                    partial_matches[skill] = similarity
                else:
                    must_have_missing.add(skill)
        
        nice_to_have_matched = nice_to_have.intersection(cv_skills_all)
        nice_to_have_missing = nice_to_have - cv_skills_all
        
        # Experience weighting (only for raw skills, not implied)
        experience_scores = {}
        for skill in must_have_matched:
            if skill in cv_skills_raw:  # Only if explicitly mentioned
                years = self.calculate_experience_weight(resume_text, skill)
                if years > 0:
                    experience_scores[skill] = years
        
        # Semantic similarity
        semantic_analysis = self.semantic_similarity_scored(job_description, resume_text)
        
        # Calculate weighted scores with PARTIAL CREDIT
        total_requirements = len(must_have) + len(or_groups)
        
        if total_requirements == 0:
            must_have_score = 100.0
        else:
            # Full credit for exact matches
            individual_matched = len([s for s in must_have if s in must_have_matched])
            or_groups_matched = sum(1 for g in or_groups.values() if any(s in cv_skills_all for s in g))
            
            # Partial credit for related skills
            partial_credit = sum(partial_matches.values())
            
            matched_requirements = individual_matched + or_groups_matched + partial_credit
            must_have_score = min((matched_requirements / total_requirements * 100), 100.0)
        
        # Nice-to-have score (bonus, not penalty if missing)
        nice_to_have_score = (len(nice_to_have_matched) / len(nice_to_have) * 100) if nice_to_have else 0
        
        # Semantic similarity
        semantic_score = semantic_analysis['overall']
        
        # Experience bonus (realistic cap at 15 points)
        total_exp_years = sum(experience_scores.values())
        avg_experience = total_exp_years / max(len(must_have_matched), 1)
        
        if avg_experience >= 5:
            experience_bonus = 15.0  # Senior level
        elif avg_experience >= 3:
            experience_bonus = 10.0  # Mid level
        elif avg_experience >= 1:
            experience_bonus = 5.0   # Junior level
        else:
            experience_bonus = 0.0   # Entry level or no experience data
        
        # BALANCED SCORING FORMULA
        # Must-have: 50% (core requirement)
        # Semantic: 20% (context and fit)
        # Nice-to-have: 10% (bonus skills)
        # Experience: 15% (seniority level)
        # Completeness: 5% (resume quality)
        final_score = (
            must_have_score * 0.50 +
            semantic_score * 0.20 +
            nice_to_have_score * 0.10 +
            experience_bonus * 1.0 +
            min(len(cv_skills_raw) / max(len(jd_skills_all), 1) * 100, 100) * 0.05
        )
        
        # Generate insights
        insights = self._generate_insights(
            must_have_matched, must_have_missing,
            nice_to_have_matched, semantic_score,
            experience_scores, or_groups, partial_matches
        )
        
        return {
            'overall_score': round(min(final_score, 100), 2),
            'breakdown': {
                'must_have_skills': round(must_have_score, 2),
                'nice_to_have_skills': round(nice_to_have_score, 2),
                'semantic_match': round(semantic_score, 2),
                'experience_bonus': round(experience_bonus, 2)
            },
            'must_have_matched': sorted(list(must_have_matched)),
            'must_have_missing': sorted(list(must_have_missing)),
            'must_have_partial': {k: f"{v*100:.0f}%" for k, v in partial_matches.items()},
            'nice_to_have_matched': sorted(list(nice_to_have_matched)),
            'nice_to_have_missing': sorted(list(nice_to_have_missing)),
            'experience_details': experience_scores,
            'insights': insights,
            'section_scores': semantic_analysis.get('sections', {}),
            'or_groups_detected': or_groups
        }
    
    def _generate_insights(self, must_matched, must_missing, nice_matched, 
                          semantic_score, experience_scores, or_groups, partial_matches=None):
        """BALANCED: Generate fair, informative insights"""
        insights = []
        
        if partial_matches is None:
            partial_matches = {}
        
        # Analyze skill match quality
        total_required = len(must_matched) + len(must_missing) + len(partial_matches)
        
        if len(must_missing) == 0 and len(partial_matches) == 0:
            insights.append("✅ Perfect match: All required skills present")
        elif len(must_missing) == 0 and len(partial_matches) > 0:
            insights.append(f"✅ Strong match: Has related skills for {len(partial_matches)} requirement(s)")
        elif len(must_missing) <= 2 and total_required > 0:
            match_rate = (len(must_matched) + len(partial_matches)) / total_required
            if match_rate >= 0.8:
                insights.append(f"✓ Good match: Minor gaps in {len(must_missing)} skill(s)")
            else:
                missing_str = ', '.join(list(must_missing)[:2])
                insights.append(f"⚠️ Missing: {missing_str}")
        elif len(must_missing) > 2:
            insights.append(f"⚠️ Skill gap: {len(must_missing)} required skills not found")
        
        # Partial match details
        if partial_matches:
            partial_skills = list(partial_matches.keys())[:2]
            insights.append(f"📚 Has related experience in: {', '.join(partial_skills)}")
        
        # Experience level assessment
        if experience_scores:
            avg_exp = np.mean(list(experience_scores.values()))
            max_exp = max(experience_scores.values())
            if max_exp >= 5:
                insights.append(f"💼 Senior level: {max_exp}+ years in key skills")
            elif avg_exp >= 3:
                insights.append(f"💼 Mid level: ~{avg_exp:.0f} years average experience")
            elif avg_exp >= 1:
                insights.append(f"📚 Junior level: ~{avg_exp:.0f} years experience")
            else:
                insights.append(f"🌱 Entry level candidate")
        else:
            insights.append("📋 Experience details not specified in resume")
        
        # Contextual fit
        if semantic_score > 80:
            insights.append("🎯 Excellent cultural and contextual fit")
        elif semantic_score > 65:
            insights.append("✓ Good overall alignment with role")
        elif semantic_score > 50:
            insights.append("⚡ Moderate fit - review context carefully")
        else:
            insights.append("⚠️ Limited contextual alignment")
        
        # Nice-to-have bonus
        if len(nice_matched) >= 3:
            insights.append(f"⭐ Bonus: {len(nice_matched)} preferred skills found")
        elif len(nice_matched) > 0:
            insights.append(f"➕ Has {len(nice_matched)} additional preferred skill(s)")
        
        return insights


# Singleton instance
_matcher = None

def get_matcher():
    global _matcher
    if _matcher is None:
        _matcher = EnterpriseATSMatcher()
    return _matcher


def analyze_resume(job_description, resume_text):
    """Main entry point for analysis"""
    matcher = get_matcher()
    return matcher.analyze_resume(job_description, resume_text)