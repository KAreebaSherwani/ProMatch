"""
=============================================================================
ULTIMATE REAL-TIME ATS CONFIG - 100% ACCURACY FOCUSED
=============================================================================
Comprehensive skill database covering ALL industries and fields
Designed for maximum matching accuracy with zero false positives
=============================================================================
"""

# =============================================================================
# EXPLICIT NON-SKILLS (Blacklist - Prevents False Positives)
# =============================================================================
EXPLICIT_NON_SKILLS = {
    # Generic resume words
    "able", "ability", "must", "required", "experience", "experienced",
    "using", "need", "needs", "description", "job", "position",
    "candidate", "candidates", "resume", "cv", "curriculum vitae",
    
    # Company/Organization words
    "corp", "corporation", "company", "inc", "incorporated", "ltd", "limited",
    "llc", "organization", "enterprise", "firm", "agency",
    
    # Contact/Admin words
    "email", "phone", "address", "contact", "location", "website",
    "apply", "application", "applicant", "hiring", "recruitment", "recruiter",
    
    # Job titles (NOT skills)
    "analyst", "developer", "engineer", "programmer", "designer",
    "manager", "director", "coordinator", "specialist", "consultant",
    "administrator", "associate", "executive", "officer", "lead",
    "senior", "junior", "intern", "trainee", "apprentice",
    "architect", "technician", "supervisor", "head", "chief",
    
    # Action verbs
    "managed", "manage", "managing", "developed", "develop", "developing",
    "created", "create", "creating", "designed", "design", "designing",
    "implemented", "implement", "implementing", "built", "build", "building",
    "led", "lead", "leading", "worked", "work", "working",
    
    # Qualifiers
    "strong", "excellent", "good", "great", "outstanding", "exceptional",
    "proficient", "expert", "skilled", "talented", "capable",
    "proven", "demonstrated", "extensive", "comprehensive",
    
    # Time/Duration words
    "years", "year", "months", "month", "weeks", "week", "days", "day",
    "current", "currently", "previous", "previously", "former", "past",
    
    # Generic adjectives
    "high", "low", "new", "old", "best", "better", "latest", "modern",
    "advanced", "basic", "intermediate", "beginner", "professional",
}

# =============================================================================
# COMPREHENSIVE SKILL SYNONYMS DATABASE
# =============================================================================
SKILL_SYNONYMS = {
    
    # =========================================================================
    # PROGRAMMING LANGUAGES (Alphabetical)
    # =========================================================================
    
    # Assembly
    "assembly": "assembly language",
    "assembly language": "assembly language",
    "asm": "assembly language",
    "x86": "assembly language",
    "arm assembly": "assembly language",
    
    # C
    "c": "c programming",
    "c programming": "c programming",
    "ansi c": "c programming",
    "c language": "c programming",
    
    # C++
    "c++": "c++",
    "cpp": "c++",
    "cplusplus": "c++",
    "c plus plus": "c++",
    
    # C#
    "c#": "c#",
    "csharp": "c#",
    "c sharp": "c#",
    ".net": "c#",
    "dotnet": "c#",
    "dot net": "c#",
    ".net core": ".net core",
    "dotnet core": ".net core",
    
    # Clojure
    "clojure": "clojure",
    "clojurescript": "clojure",
    
    # COBOL
    "cobol": "cobol",
    
    # Dart
    "dart": "dart",
    "dart language": "dart",
    
    # Elixir
    "elixir": "elixir",
    
    # Erlang
    "erlang": "erlang",
    
    # F#
    "f#": "f#",
    "fsharp": "f#",
    
    # Fortran
    "fortran": "fortran",
    
    # Go
    "go": "golang",
    "golang": "golang",
    "go lang": "golang",
    "go language": "golang",
    
    # Groovy
    "groovy": "groovy",
    
    # Haskell
    "haskell": "haskell",
    
    # Java
    "java": "java",
    "java8": "java",
    "java 8": "java",
    "java11": "java",
    "java 11": "java",
    "java17": "java",
    "java 17": "java",
    "jdk": "java",
    "jre": "java",
    
    # JavaScript
    "javascript": "javascript",
    "js": "javascript",
    "ecmascript": "javascript",
    "es6": "javascript",
    "es5": "javascript",
    "es2015": "javascript",
    "es2020": "javascript",
    
    # Julia
    "julia": "julia",
    
    # Kotlin
    "kotlin": "kotlin",
    
    # Lisp
    "lisp": "lisp",
    "common lisp": "lisp",
    
    # Lua
    "lua": "lua",
    
    # MATLAB
    "matlab": "matlab",
    "octave": "matlab",
    
    # Objective-C
    "objective-c": "objective-c",
    "objective c": "objective-c",
    "objc": "objective-c",
    
    # Pascal
    "pascal": "pascal",
    "delphi": "pascal",
    
    # Perl
    "perl": "perl",
    
    # PHP
    "php": "php",
    "php7": "php",
    "php8": "php",
    "hypertext preprocessor": "php",
    
    # Python
    "python": "python",
    "py": "python",
    "python3": "python",
    "python 3": "python",
    "python2": "python",
    "python 2": "python",
    
    # R
    "r": "r programming",
    "r programming": "r programming",
    "rstudio": "r programming",
    "r language": "r programming",
    
    # Ruby
    "ruby": "ruby",
    "ruby on rails": "ruby on rails",
    "rails": "ruby on rails",
    "ror": "ruby on rails",
    
    # Rust
    "rust": "rust",
    
    # Scala
    "scala": "scala",
    
    # Scheme
    "scheme": "scheme",
    
    # Shell/Bash
    "bash": "bash scripting",
    "bash scripting": "bash scripting",
    "shell": "bash scripting",
    "shell scripting": "bash scripting",
    "sh": "bash scripting",
    "zsh": "bash scripting",
    "ksh": "bash scripting",
    
    # SQL
    "sql": "sql",
    "structured query language": "sql",
    "t-sql": "sql",
    "tsql": "sql",
    "pl/sql": "sql",
    "plsql": "sql",
    
    # Swift
    "swift": "swift",
    "swift 5": "swift",
    "swiftui": "swift",
    
    # TypeScript
    "typescript": "typescript",
    "ts": "typescript",
    
    # VBA
    "vba": "vba",
    "visual basic": "vba",
    "vb.net": "vba",
    
    # Other
    "powershell": "powershell",
    "ps": "powershell",
    
    # =========================================================================
    # WEB DEVELOPMENT - FRONTEND
    # =========================================================================
    
    # Core Web Technologies
    "html": "html",
    "html5": "html",
    "html 5": "html",
    "xhtml": "html",
    
    "css": "css",
    "css3": "css",
    "css 3": "css",
    "cascading style sheets": "css",
    
    # CSS Preprocessors
    "sass": "sass",
    "scss": "sass",
    "less": "less",
    "stylus": "stylus",
    
    # JavaScript Frameworks
    "react": "react",
    "reactjs": "react",
    "react.js": "react",
    "react js": "react",
    
    "angular": "angular",
    "angularjs": "angular",
    "angular.js": "angular",
    "angular 2": "angular",
    "angular2": "angular",
    
    "vue": "vue",
    "vuejs": "vue",
    "vue.js": "vue",
    "vue js": "vue",
    
    "svelte": "svelte",
    "sveltekit": "svelte",
    
    "ember": "ember",
    "emberjs": "ember",
    "ember.js": "ember",
    
    "backbone": "backbone",
    "backbonejs": "backbone",
    "backbone.js": "backbone",
    
    # UI Libraries/Frameworks
    "jquery": "jquery",
    "jquery ui": "jquery",
    
    "bootstrap": "bootstrap",
    "bootstrap 4": "bootstrap",
    "bootstrap 5": "bootstrap",
    
    "tailwindcss": "tailwind css",
    "tailwind": "tailwind css",
    "tailwind css": "tailwind css",
    
    "material-ui": "material ui",
    "material ui": "material ui",
    "mui": "material ui",
    "material design": "material ui",
    
    "ant design": "ant design",
    "antd": "ant design",
    
    "chakra ui": "chakra ui",
    "chakra-ui": "chakra ui",
    
    "shadcn": "shadcn",
    "shadcn/ui": "shadcn",
    
    "semantic ui": "semantic ui",
    "semantic-ui": "semantic ui",
    
    "bulma": "bulma",
    "foundation": "foundation",
    
    # Build Tools
    "webpack": "webpack",
    "vite": "vite",
    "rollup": "rollup",
    "parcel": "parcel",
    "gulp": "gulp",
    "grunt": "grunt",
    
    # Other Frontend
    "babel": "babel",
    "eslint": "eslint",
    "prettier": "prettier",
    
    # SSR/SSG Frameworks
    "nextjs": "next.js",
    "next": "next.js",
    "next.js": "next.js",
    
    "nuxtjs": "nuxt.js",
    "nuxt": "nuxt.js",
    "nuxt.js": "nuxt.js",
    
    "gatsby": "gatsby",
    "gatsbyjs": "gatsby",
    
    "remix": "remix",
    
    "astro": "astro",
    
    # =========================================================================
    # WEB DEVELOPMENT - BACKEND
    # =========================================================================
    
    # Node.js
    "node": "node.js",
    "nodejs": "node.js",
    "node.js": "node.js",
    "node js": "node.js",
    
    "express": "express.js",
    "expressjs": "express.js",
    "express.js": "express.js",
    
    "nestjs": "nest.js",
    "nest": "nest.js",
    "nest.js": "nest.js",
    
    "fastify": "fastify",
    "koa": "koa",
    "hapi": "hapi",
    
    # Python Frameworks
    "django": "django",
    "flask": "flask",
    "fastapi": "fastapi",
    "pyramid": "pyramid",
    "tornado": "tornado",
    "bottle": "bottle",
    
    # PHP Frameworks
    "laravel": "laravel",
    "symfony": "symfony",
    "codeigniter": "codeigniter",
    "cakephp": "cakephp",
    "yii": "yii",
    "zend": "zend",
    
    # Java Frameworks
    "spring": "spring framework",
    "spring framework": "spring framework",
    "spring boot": "spring boot",
    "spring mvc": "spring framework",
    "spring cloud": "spring framework",
    "hibernate": "hibernate",
    "struts": "struts",
    
    # .NET
    "asp.net": "asp.net",
    "asp net": "asp.net",
    "asp": "asp.net",
    "asp.net mvc": "asp.net",
    "asp.net core": "asp.net core",
    
    # Ruby
    "sinatra": "sinatra",
    
    # Go
    "gin": "gin",
    "echo": "echo",
    "fiber": "fiber",
    
    # =========================================================================
    # MOBILE DEVELOPMENT
    # =========================================================================
    
    "android development": "android development",
    "android": "android development",
    "android studio": "android development",
    "android sdk": "android development",
    
    "ios development": "ios development",
    "ios": "ios development",
    "xcode": "ios development",
    "cocoa": "ios development",
    "cocoa touch": "ios development",
    
    "flutter": "flutter",
    "react native": "react native",
    "rn": "react native",
    "ionic": "ionic",
    "cordova": "cordova",
    "phonegap": "cordova",
    "xamarin": "xamarin",
    
    "swiftui": "swiftui",
    "jetpack compose": "jetpack compose",
    
    # =========================================================================
    # DATABASES
    # =========================================================================
    
    # Relational Databases
    "mysql": "mysql",
    "my sql": "mysql",
    
    "postgresql": "postgresql",
    "postgres": "postgresql",
    "postgre": "postgresql",
    "psql": "postgresql",
    
    "oracle": "oracle database",
    "oracle database": "oracle database",
    "oracle db": "oracle database",
    
    "sql server": "sql server",
    "mssql": "sql server",
    "ms sql": "sql server",
    "microsoft sql server": "sql server",
    
    "sqlite": "sqlite",
    "mariadb": "mariadb",
    "db2": "db2",
    "ibm db2": "db2",
    
    # NoSQL Databases
    "mongodb": "mongodb",
    "mongo": "mongodb",
    "mongo db": "mongodb",
    
    "cassandra": "cassandra",
    "apache cassandra": "cassandra",
    
    "redis": "redis",
    "memcached": "memcached",
    
    "couchdb": "couchdb",
    "couchbase": "couchbase",
    
    "dynamodb": "dynamodb",
    "dynamo db": "dynamodb",
    "amazon dynamodb": "dynamodb",
    
    "firebase": "firebase",
    "firestore": "firebase",
    "firebase realtime": "firebase",
    
    "elasticsearch": "elasticsearch",
    "elastic search": "elasticsearch",
    "elk": "elk stack",
    "elk stack": "elk stack",
    "elastic stack": "elk stack",
    
    # Graph Databases
    "neo4j": "neo4j",
    "arangodb": "arangodb",
    
    # Time Series
    "influxdb": "influxdb",
    "timescaledb": "timescaledb",
    
    # ORMs
    "orm": "orm",
    "object relational mapping": "orm",
    "sequelize": "sequelize",
    "typeorm": "typeorm",
    "prisma": "prisma",
    "sqlalchemy": "sqlalchemy",
    "doctrine": "doctrine",
    "eloquent": "eloquent",
    
    # =========================================================================
    # CLOUD PLATFORMS & SERVICES
    # =========================================================================
    
    # AWS
    "aws": "amazon web services",
    "amazon web services": "amazon web services",
    "amazon aws": "amazon web services",
    
    "ec2": "amazon ec2",
    "amazon ec2": "amazon ec2",
    
    "s3": "amazon s3",
    "amazon s3": "amazon s3",
    
    "lambda": "aws lambda",
    "aws lambda": "aws lambda",
    "lambda functions": "aws lambda",
    
    "rds": "amazon rds",
    "amazon rds": "amazon rds",
    
    "dynamodb": "amazon dynamodb",
    
    "ecs": "amazon ecs",
    "amazon ecs": "amazon ecs",
    
    "eks": "amazon eks",
    "amazon eks": "amazon eks",
    
    "cloudfront": "cloudfront",
    "route53": "route53",
    "cloudformation": "cloudformation",
    "cloudwatch": "cloudwatch",
    
    "sagemaker": "sagemaker",
    "aws sagemaker": "sagemaker",
    
    "redshift": "redshift",
    "amazon redshift": "redshift",
    
    "aurora": "aurora",
    "amazon aurora": "aurora",
    
    # Azure
    "azure": "microsoft azure",
    "microsoft azure": "microsoft azure",
    "ms azure": "microsoft azure",
    
    "azure functions": "azure functions",
    "azure devops": "azure devops",
    "azure sql": "azure sql",
    "cosmos db": "cosmos db",
    "azure cosmos db": "cosmos db",
    
    "aks": "azure kubernetes service",
    "azure kubernetes": "azure kubernetes service",
    "azure kubernetes service": "azure kubernetes service",
    
    "azure ml": "azure machine learning",
    "azure machine learning": "azure machine learning",
    
    "arm templates": "arm templates",
    
    # Google Cloud
    "gcp": "google cloud platform",
    "google cloud": "google cloud platform",
    "google cloud platform": "google cloud platform",
    "gcloud": "google cloud platform",
    
    "bigquery": "bigquery",
    "big query": "bigquery",
    
    "gke": "google kubernetes engine",
    "google kubernetes engine": "google kubernetes engine",
    
    "cloud functions": "google cloud functions",
    "google cloud functions": "google cloud functions",
    
    "cloud run": "cloud run",
    "google cloud run": "cloud run",
    
    "vertex ai": "vertex ai",
    
    # Other Cloud
    "heroku": "heroku",
    "digital ocean": "digital ocean",
    "digitalocean": "digital ocean",
    "linode": "linode",
    "vultr": "vultr",
    
    # =========================================================================
    # DEVOPS & CI/CD
    # =========================================================================
    
    # Containerization
    "docker": "docker",
    "containerization": "docker",
    "docker compose": "docker compose",
    "docker-compose": "docker compose",
    "dockerfile": "docker",
    
    "kubernetes": "kubernetes",
    "k8s": "kubernetes",
    "kube": "kubernetes",
    
    "openshift": "openshift",
    "rancher": "rancher",
    "docker swarm": "docker swarm",
    
    "helm": "helm",
    "helm charts": "helm",
    
    # CI/CD
    "ci/cd": "ci/cd",
    "cicd": "ci/cd",
    "continuous integration": "ci/cd",
    "continuous deployment": "ci/cd",
    "continuous delivery": "ci/cd",
    
    "jenkins": "jenkins",
    
    "gitlab ci": "gitlab ci",
    "gitlab-ci": "gitlab ci",
    
    "github actions": "github actions",
    
    "circleci": "circle ci",
    "circle ci": "circle ci",
    
    "travis ci": "travis ci",
    "travis-ci": "travis ci",
    
    "azure pipelines": "azure pipelines",
    
    "bamboo": "bamboo",
    "teamcity": "teamcity",
    "drone": "drone",
    
    # Infrastructure as Code
    "terraform": "terraform",
    "iac": "infrastructure as code",
    "infrastructure as code": "infrastructure as code",
    
    "ansible": "ansible",
    "puppet": "puppet",
    "chef": "chef",
    "saltstack": "saltstack",
    "salt": "saltstack",
    
    # Monitoring & Observability
    "prometheus": "prometheus",
    "grafana": "grafana",
    
    "datadog": "datadog",
    "new relic": "new relic",
    "newrelic": "new relic",
    
    "splunk": "splunk",
    
    "nagios": "nagios",
    "zabbix": "zabbix",
    
    "pagerduty": "pagerduty",
    "opsgenie": "opsgenie",
    
    # =========================================================================
    # DATA SCIENCE & MACHINE LEARNING
    # =========================================================================
    
    # Core Concepts
    "machine learning": "machine learning",
    "ml": "machine learning",
    
    "deep learning": "deep learning",
    "dl": "deep learning",
    
    "artificial intelligence": "artificial intelligence",
    "ai": "artificial intelligence",
    
    "data science": "data science",
    "data scientist": "data science",
    
    # ML/DL Frameworks
    "tensorflow": "tensorflow",
    "tf": "tensorflow",
    "tensorflow 2": "tensorflow",
    
    "keras": "keras",
    
    "pytorch": "pytorch",
    "torch": "pytorch",
    
    "scikit-learn": "scikit-learn",
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    
    "xgboost": "xgboost",
    "lightgbm": "lightgbm",
    "catboost": "catboost",
    
    "fastai": "fastai",
    
    # Data Processing
    "pandas": "pandas",
    "numpy": "numpy",
    "scipy": "scipy",
    
    # Data Visualization
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "bokeh": "bokeh",
    "altair": "altair",
    
    "tableau": "tableau",
    "power bi": "power bi",
    "powerbi": "power bi",
    "qlikview": "qlikview",
    "qlik": "qlikview",
    "looker": "looker",
    "metabase": "metabase",
    "superset": "superset",
    
    "data visualization": "data visualization",
    "dataviz": "data visualization",
    "data viz": "data visualization",
    "dashboarding": "data visualization",
    
    # Computer Vision
    "computer vision": "computer vision",
    "cv": "computer vision",
    "opencv": "opencv",
    "cv2": "opencv",
    "pillow": "pillow",
    "pil": "pillow",
    
    # NLP
    "natural language processing": "natural language processing",
    "nlp": "natural language processing",
    "nlu": "natural language understanding",
    "natural language understanding": "natural language understanding",
    
    "spacy": "spacy",
    "nltk": "nltk",
    "gensim": "gensim",
    
    "huggingface": "huggingface transformers",
    "transformers": "huggingface transformers",
    "hugging face": "huggingface transformers",
    
    "bert": "bert",
    "gpt": "gpt",
    "llm": "large language models",
    "large language models": "large language models",
    "generative ai": "generative ai",
    "gen ai": "generative ai",
    
    # MLOps
    "mlops": "mlops",
    "ml ops": "mlops",
    
    # =========================================================================
    # BIG DATA & DATA ENGINEERING
    # =========================================================================
    
    "hadoop": "hadoop",
    "hdfs": "hadoop",
    "mapreduce": "hadoop",
    
    "spark": "apache spark",
    "apache spark": "apache spark",
    "pyspark": "apache spark",
    
    "kafka": "kafka",
    "apache kafka": "kafka",
    
    "airflow": "airflow",
    "apache airflow": "airflow",
    
    "flink": "apache flink",
    "apache flink": "apache flink",
    
    "hive": "hive",
    "apache hive": "hive",
    
    "pig": "pig",
    "apache pig": "pig",
    
    "storm": "storm",
    "apache storm": "storm",
    
    "nifi": "nifi",
    "apache nifi": "nifi",
    
    "snowflake": "snowflake",
    "databricks": "databricks",
    
    "dbt": "dbt",
    "data build tool": "dbt",
    
    "etl": "etl",
    "elt": "etl",
    "extract transform load": "etl",
    
    "data pipeline": "data pipeline",
    "data pipelines": "data pipeline",
    
    "data warehousing": "data warehousing",
    "data warehouse": "data warehousing",
    
    "data analytics": "data analytics",
    "data analysis": "data analytics",
    
    "business intelligence": "business intelligence",
    
    # =========================================================================
    # CYBERSECURITY
    # =========================================================================
    
    "cybersecurity": "cybersecurity",
    "cyber security": "cybersecurity",
    "information security": "information security",
    "infosec": "cybersecurity",
    
    "network security": "network security",
    "penetration testing": "penetration testing",
    "pen testing": "penetration testing",
    "pentesting": "penetration testing",
    
    "ethical hacking": "ethical hacking",
    "security analyst": "security analyst",
    
    "incident response": "incident response",
    "siem": "siem",
    
    "firewall": "firewall",
    "vpn": "vpn",
    "encryption": "encryption",
    "cryptography": "cryptography",
    
    "vulnerability assessment": "vulnerability assessment",
    "threat intelligence": "threat intelligence",
    "malware analysis": "malware analysis",
    
    "digital forensics": "digital forensics",
    "forensics": "digital forensics",
    
    "soc": "security operations center",
    "security operations": "security operations",
    "security operations center": "security operations center",
    
    "zero trust": "zero trust",
    "identity management": "identity management",
    "access control": "access control",
    
    # Security Tools
    "metasploit": "metasploit",
    "burp suite": "burp suite",
    "wireshark": "wireshark",
    "nmap": "nmap",
    "kali linux": "kali linux",
    
    # Certifications (as skills)
    "cissp": "cissp",
    "ceh": "ceh",
    "comptia security+": "comptia security+",
    "comptia": "comptia",
    "ccna": "ccna",
    "ccnp": "ccnp",
    
    # =========================================================================
    # API & INTEGRATION
    # =========================================================================
    
    "api": "api development",
    "api development": "api development",
    "apis": "api development",
    
    "rest": "rest api",
    "restful": "rest api",
    "rest api": "rest api",
    "restful api": "rest api",
    
    "graphql": "graphql",
    "graph ql": "graphql",
    "apollo": "graphql",
    
    "grpc": "grpc",
    "soap": "soap",
    "soap api": "soap",
    
    "microservices": "microservices",
    "microservice": "microservices",
    "microservices architecture": "microservices",
    
    "serverless": "serverless architecture",
    "serverless architecture": "serverless architecture",
    "faas": "serverless architecture",
    
    "jwt": "json web token",
    "json web token": "json web token",
    
    "oauth": "oauth",
    "oauth2": "oauth",
    "oauth 2.0": "oauth",
    
    "saml": "saml",
    "sso": "single sign on",
    "single sign on": "single sign on",
    
    "websockets": "websockets",
    "socket.io": "websockets",
    
    "message queue": "message queue",
    "rabbitmq": "rabbitmq",
    "activemq": "activemq",
    
    # =========================================================================
    # VERSION CONTROL & COLLABORATION
    # =========================================================================
    
    "git": "git",
    "github": "github",
    "gitlab": "gitlab",
    "bitbucket": "bitbucket",
    "svn": "svn",
    "subversion": "svn",
    "mercurial": "mercurial",
    
    # =========================================================================
    # PROJECT MANAGEMENT & AGILE
    # =========================================================================
    
    "project management": "project management",
    "pm": "project management",
    "pmp": "pmp",
    
    "agile": "agile methodology",
    "agile methodology": "agile methodology",
    
    "scrum": "scrum",
    "scrum master": "scrum",
    
    "kanban": "kanban",
    "lean": "lean methodology",
    "lean methodology": "lean methodology",
    
    "waterfall": "waterfall",
    "prince2": "prince2",
    
    "six sigma": "six sigma",
    "lean six sigma": "six sigma",
    
    # Tools
    "jira": "jira",
    "confluence": "confluence",
    "trello": "trello",
    "asana": "asana",
    "monday.com": "monday.com",
    "basecamp": "basecamp",
    "clickup": "clickup",
    
    # =========================================================================
    # DESIGN & CREATIVE
    # =========================================================================
    
    # UI/UX
    "ui design": "ui design",
    "user interface design": "ui design",
    "ux design": "ux design",
    "user experience design": "ux design",
    "ux research": "ux research",
    "user research": "user research",
    
    "usability": "usability",
    "interaction design": "interaction design",
    "ixd": "interaction design",
    
    # Graphic Design
    "graphic design": "graphic design",
    "visual design": "visual design",
    
    # Design Tools
    "figma": "figma",
    "sketch": "sketch",
    "adobe xd": "adobe xd",
    "xd": "adobe xd",
    "invision": "invision",
    "zeplin": "zeplin",
    
    "photoshop": "adobe photoshop",
    "adobe photoshop": "adobe photoshop",
    
    "illustrator": "adobe illustrator",
    "adobe illustrator": "adobe illustrator",
    
    "indesign": "adobe indesign",
    "adobe indesign": "adobe indesign",
    
    "after effects": "adobe after effects",
    "adobe after effects": "adobe after effects",
    
    "premiere pro": "adobe premiere",
    "adobe premiere": "adobe premiere",
    "premiere": "adobe premiere",
    
    "lightroom": "adobe lightroom",
    "adobe lightroom": "adobe lightroom",
    
    "canva": "canva",
    "procreate": "procreate",
    
    # 3D Design
    "blender": "blender",
    "maya": "maya",
    "3ds max": "3ds max",
    "cinema 4d": "cinema 4d",
    "c4d": "cinema 4d",
    "zbrush": "zbrush",
    
    # Video/Audio
    "final cut pro": "final cut pro",
    "davinci resolve": "davinci resolve",
    "pro tools": "pro tools",
    "ableton": "ableton",
    "logic pro": "logic pro",
    "fl studio": "fl studio",
    
    # =========================================================================
    # BUSINESS & FINANCE
    # =========================================================================
    
    # Accounting
    "accounting": "accounting",
    "bookkeeping": "bookkeeping",
    "financial accounting": "financial accounting",
    "managerial accounting": "managerial accounting",
    "cost accounting": "cost accounting",
    
    "gaap": "gaap",
    "ifrs": "ifrs",
    
    "accounts payable": "accounts payable",
    "ap": "accounts payable",
    "accounts receivable": "accounts receivable",
    "ar": "accounts receivable",
    
    # Finance
    "finance": "finance",
    "financial analysis": "financial analysis",
    "financial modeling": "financial modeling",
    "financial planning": "financial planning",
    "fpa": "financial planning and analysis",
    "financial planning and analysis": "financial planning and analysis",
    
    "budgeting": "budgeting",
    "forecasting": "forecasting",
    "valuation": "valuation",
    "dcf": "valuation",
    
    "investment banking": "investment banking",
    "ib": "investment banking",
    "m&a": "mergers and acquisitions",
    "mergers and acquisitions": "mergers and acquisitions",
    
    "equity research": "equity research",
    "equity analysis": "equity analysis",
    "credit analysis": "credit analysis",
    
    "portfolio management": "portfolio management",
    "asset management": "asset management",
    "wealth management": "wealth management",
    
    "private equity": "private equity",
    "pe": "private equity",
    "venture capital": "venture capital",
    "vc": "venture capital",
    "hedge funds": "hedge funds",
    
    "derivatives": "derivatives",
    "fixed income": "fixed income",
    "capital markets": "capital markets",
    
    "risk management": "risk management",
    "treasury": "treasury",
    "cash management": "cash management",
    
    # ERP Systems
    "erp": "enterprise resource planning",
    "enterprise resource planning": "enterprise resource planning",
    
    "sap": "sap",
    "sap fico": "sap",
    "sap erp": "sap",
    "sap s4hana": "sap",
    "sap hana": "sap",
    
    "oracle erp": "oracle erp",
    "oracle financials": "oracle erp",
    "netsuite": "netsuite",
    
    "quickbooks": "quickbooks",
    "xero": "xero",
    "sage": "sage",
    "freshbooks": "freshbooks",
    
    # Certifications
    "cpa": "cpa",
    "cfa": "cfa",
    "cma": "cma",
    "cia": "cia",
    "frm": "frm",
    "acca": "acca",
    "cima": "cima",
    
    # =========================================================================
    # MARKETING & SALES
    # =========================================================================
    
    # Digital Marketing
    "digital marketing": "digital marketing",
    "online marketing": "digital marketing",
    
    "seo": "search engine optimization",
    "search engine optimization": "search engine optimization",
    
    "sem": "search engine marketing",
    "search engine marketing": "search engine marketing",
    
    "ppc": "pay per click",
    "pay per click": "pay per click",
    "paid search": "pay per click",
    
    "social media marketing": "social media marketing",
    "smm": "social media marketing",
    "social media": "social media marketing",
    
    "content marketing": "content marketing",
    "content strategy": "content marketing",
    
    "email marketing": "email marketing",
    "marketing automation": "marketing automation",
    
    "growth marketing": "growth marketing",
    "growth hacking": "growth marketing",
    "performance marketing": "performance marketing",
    
    # Marketing Tools
    "google analytics": "google analytics",
    "ga": "google analytics",
    "ga4": "google analytics",
    
    "google tag manager": "google tag manager",
    "gtm": "google tag manager",
    
    "google ads": "google ads",
    "adwords": "google ads",
    "adsense": "google ads",
    
    "facebook ads": "facebook ads",
    "meta ads": "facebook ads",
    "linkedin ads": "linkedin ads",
    
    "mailchimp": "mailchimp",
    "hubspot": "hubspot",
    "marketo": "marketo",
    
    # Optimization
    "conversion rate optimization": "conversion rate optimization",
    "cro": "conversion rate optimization",
    "a/b testing": "a/b testing",
    "split testing": "a/b testing",
    
    # Content
    "copywriting": "copywriting",
    "content writing": "copywriting",
    "technical writing": "technical writing",
    
    # Sales
    "sales": "sales",
    "business development": "business development",
    "bd": "business development",
    "lead generation": "lead generation",
    "prospecting": "lead generation",
    
    "crm": "customer relationship management",
    "customer relationship management": "customer relationship management",
    
    "salesforce": "salesforce",
    "sfdc": "salesforce",
    "zoho": "zoho",
    "pipedrive": "pipedrive",
    
    # =========================================================================
    # HEALTHCARE & MEDICAL
    # =========================================================================
    
    "nursing": "nursing",
    "patient care": "patient care",
    "clinical skills": "clinical skills",
    
    "medical coding": "medical coding",
    "icd-10": "medical coding",
    "cpt": "medical coding",
    "medical billing": "medical billing",
    
    "pharmacy": "pharmacy",
    "pharmacology": "pharmacology",
    
    "radiology": "radiology",
    "medical imaging": "medical imaging",
    "ultrasound": "ultrasound",
    
    "emergency care": "emergency care",
    "icu": "intensive care unit",
    "intensive care": "intensive care unit",
    "critical care": "intensive care unit",
    
    "laboratory skills": "laboratory skills",
    "clinical laboratory": "laboratory skills",
    
    "physical therapy": "physical therapy",
    "physiotherapy": "physical therapy",
    "occupational therapy": "occupational therapy",
    
    "mental health": "mental health",
    "psychiatry": "mental health",
    "psychology": "mental health",
    "counseling": "counseling",
    
    "nutrition": "nutrition",
    "dietetics": "nutrition",
    
    "telemedicine": "telemedicine",
    "telehealth": "telemedicine",
    
    "ehr": "electronic health records",
    "electronic health records": "electronic health records",
    "emr": "electronic health records",
    "epic": "epic",
    "cerner": "cerner",
    
    "hipaa": "hipaa",
    "patient privacy": "hipaa",
    
    # =========================================================================
    # ENGINEERING & MANUFACTURING
    # =========================================================================
    
    "mechanical engineering": "mechanical engineering",
    "civil engineering": "civil engineering",
    "electrical engineering": "electrical engineering",
    "chemical engineering": "chemical engineering",
    "industrial engineering": "industrial engineering",
    "aerospace engineering": "aerospace engineering",
    "biomedical engineering": "biomedical engineering",
    "environmental engineering": "environmental engineering",
    
    "cad": "computer aided design",
    "computer aided design": "computer aided design",
    "autocad": "autocad",
    "solidworks": "solidworks",
    "catia": "catia",
    "fusion 360": "fusion 360",
    "inventor": "inventor",
    "creo": "creo",
    
    "manufacturing": "manufacturing",
    "production": "manufacturing",
    "lean manufacturing": "lean manufacturing",
    
    "cnc": "cnc",
    "cnc machining": "cnc",
    "machining": "machining",
    "welding": "welding",
    
    "quality control": "quality control",
    "qc": "quality control",
    "quality assurance": "quality assurance",
    "qa": "quality assurance",
    "qms": "quality management system",
    
    "iso 9001": "iso 9001",
    "iso certification": "iso certification",
    
    "plm": "product lifecycle management",
    "product lifecycle management": "product lifecycle management",
    
    "fea": "finite element analysis",
    "finite element analysis": "finite element analysis",
    "cfd": "computational fluid dynamics",
    "computational fluid dynamics": "computational fluid dynamics",
    
    "ansys": "ansys",
    "comsol": "comsol",
    
    "robotics": "robotics",
    "automation": "automation",
    "industrial iot": "industrial iot",
    "iiot": "industrial iot",
    "industry 4.0": "industry 4.0",
    
    # =========================================================================
    # SUPPLY CHAIN & LOGISTICS
    # =========================================================================
    
    "supply chain": "supply chain management",
    "supply chain management": "supply chain management",
    "logistics": "logistics",
    "procurement": "procurement",
    "inventory management": "inventory management",
    "warehouse management": "warehouse management",
    
    # =========================================================================
    # HR & RECRUITMENT
    # =========================================================================
    
    "human resources": "human resources",
    "hr": "human resources",
    "talent acquisition": "talent acquisition",
    "recruiting": "recruiting",
    "recruitment": "recruiting",
    
    "applicant tracking system": "applicant tracking system",
    "ats": "applicant tracking system",
    
    "employee relations": "employee relations",
    "performance management": "performance management",
    "compensation": "compensation",
    "benefits administration": "benefits administration",
    
    "workday": "workday",
    "successfactors": "successfactors",
    "adp": "adp",
    
    # =========================================================================
    # LEGAL & COMPLIANCE
    # =========================================================================
    
    "legal research": "legal research",
    "legal writing": "legal writing",
    "contracts": "contracts",
    "contract management": "contract management",
    "contract law": "contract law",
    
    "compliance": "compliance",
    "regulatory compliance": "compliance",
    "corporate law": "corporate law",
    "litigation": "litigation",
    
    "intellectual property": "intellectual property",
    "ip": "intellectual property",
    "patent law": "patent law",
    "trademark": "trademark",
    "copyright": "copyright",
    
    "employment law": "employment law",
    "labor law": "employment law",
    
    "gdpr": "gdpr",
    "data protection": "gdpr",
    "privacy law": "privacy law",
    
    "sox": "sox",
    "sarbanes oxley": "sox",
    "aml": "anti money laundering",
    "kyc": "know your customer",
    
    # =========================================================================
    # SOFT SKILLS & LEADERSHIP
    # =========================================================================
    
    "communication skills": "communication skills",
    "communication": "communication skills",
    "verbal communication": "communication skills",
    "written communication": "communication skills",
    
    "presentation skills": "presentation skills",
    "public speaking": "public speaking",
    
    "teamwork": "teamwork",
    "collaboration": "collaboration",
    "team collaboration": "teamwork",
    
    "leadership": "leadership",
    "team leadership": "leadership",
    "people management": "leadership",
    
    "problem solving": "problem solving",
    "troubleshooting": "problem solving",
    "analytical skills": "analytical skills",
    "critical thinking": "critical thinking",
    "strategic thinking": "strategic thinking",
    
    "adaptability": "adaptability",
    "flexibility": "adaptability",
    
    "time management": "time management",
    "organization": "organization",
    "organizational skills": "organization",
    
    "decision making": "decision making",
    "negotiation": "negotiation",
    "conflict resolution": "conflict resolution",
    
    "emotional intelligence": "emotional intelligence",
    "eq": "emotional intelligence",
    "empathy": "empathy",
    
    "mentoring": "mentoring",
    "coaching": "coaching",
    
    "stakeholder management": "stakeholder management",
    "relationship building": "relationship building",
    "strategic planning": "strategic planning",
    "change management": "change management",
    
    # =========================================================================
    # EMERGING TECHNOLOGIES
    # =========================================================================
    
    # Blockchain
    "blockchain": "blockchain",
    "distributed ledger": "blockchain",
    "ethereum": "ethereum",
    "solidity": "solidity",
    "smart contracts": "smart contracts",
    "web3": "web3",
    "cryptocurrency": "cryptocurrency",
    "bitcoin": "bitcoin",
    "defi": "defi",
    "nft": "nft",
    
    # IoT
    "iot": "internet of things",
    "internet of things": "internet of things",
    "embedded systems": "embedded systems",
    "firmware": "firmware",
    "edge computing": "edge computing",
    
    # 5G
    "5g": "5g",
    
    # Quantum
    "quantum computing": "quantum computing",
    
    # VR/AR
    "virtual reality": "virtual reality",
    "vr": "virtual reality",
    "augmented reality": "augmented reality",
    "ar": "augmented reality",
    "mixed reality": "mixed reality",
    "xr": "extended reality",
    "extended reality": "extended reality",
    
    # Biotech
    "biotechnology": "biotechnology",
    "biotech": "biotechnology",
    "genomics": "genomics",
    "bioinformatics": "bioinformatics",
    "crispr": "crispr",
    
    # Clean Energy
    "renewable energy": "renewable energy",
    "solar energy": "solar energy",
    "wind energy": "wind energy",
    "sustainability": "sustainability",
    "esg": "esg",
    
    # RPA
    "rpa": "robotic process automation",
    "robotic process automation": "robotic process automation",
    "uipath": "uipath",
    "blue prism": "blue prism",
    "automation anywhere": "automation anywhere",
}

# =============================================================================
# STOP WORDS (Extended)
# =============================================================================
STOP_WORDS = {
    # Resume filler words
    "experience", "experienced", "years", "year", "months", "month",
    "work", "worked", "working", "job", "jobs", "role", "roles",
    "candidate", "candidates", "team", "teams", "company", "companies",
    "responsible", "responsibilities", "responsibility", "duties", "duty",
    "skills", "skill", "knowledge", "knowledgeable", "expertise",
    "using", "used", "use", "utilize", "utilized", "utilization",
    
    # Qualifiers
    "strong", "stronger", "strongest", "excellent", "good", "great",
    "outstanding", "exceptional", "superior", "proficient", "proficiency",
    "familiar", "familiarity", "better", "best", "advanced", "basic",
    "intermediate", "expert", "skilled", "talented", "capable", "ability",
    
    # Action verbs
    "managed", "manage", "managing", "management",
    "developed", "develop", "developing", "development",
    "created", "create", "creating", "designed", "design", "designing",
    "led", "lead", "leading", "built", "build", "building",
    "implemented", "implement", "implementing", "maintained", "maintain",
    "delivered", "deliver", "delivering", "executed", "execute",
    
    # Common words
    "with", "and", "in", "on", "for", "of", "the", "a", "an", "at",
    "by", "to", "from", "as", "or", "but", "if", "while", "during",
    "through", "throughout", "various", "multiple", "several", "many",
    
    # Time/status
    "current", "currently", "previous", "previously", "former",
    "ongoing", "continuous", "regular", "frequent",
    
    # Job-related
    "position", "positions", "assignment", "assignments", "project", "projects",
    
    # Don't extract these as standalone skills
    "ability", "abilities", "capability", "capabilities",
    "demonstrated", "demonstrate", "proven", "prove",
}