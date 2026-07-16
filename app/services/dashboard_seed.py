from __future__ import annotations

from app.db.mongodb import get_db


DEFAULT_CAPABILITIES = [
    {
        "_id": "custom-ai-agents",
        "title": "Custom AI Agents",
        "description": "Autonomous digital employees tailored to your business logic and operational goals.",
        "icon": "AI",
        "link": "#services",
        "enabled": True,
    },
    {
        "_id": "llm-specialization",
        "title": "LLM Specialization",
        "description": "Fine-tuning and deploying advanced LLMs for context-specific, high-performance tasks.",
        "icon": "LLM",
        "link": "#services",
        "enabled": True,
    },
    {
        "_id": "workflow-automation",
        "title": "Workflow Automation",
        "description": "Streamlining legacy environments with intelligent, self-correcting software bridges.",
        "icon": "WF",
        "link": "#services",
        "enabled": True,
    },
    {
        "_id": "enterprise-web",
        "title": "Enterprise Web",
        "description": "Scalable, high-fidelity web applications with a foundation of performance and security.",
        "icon": "EW",
        "link": "#services",
        "enabled": True,
    },
]

DEFAULT_INNOVATORS = [
    {"_id": "metalogic", "name": "METALOGIC", "enabled": True},
    {"_id": "cloudrise", "name": "CLOUDRISE", "enabled": True},
    {"_id": "zenith-ai", "name": "ZENITH AI", "enabled": True},
    {"_id": "novasphere", "name": "NOVASPHERE", "enabled": True},
    {"_id": "velocity", "name": "VELOCITY", "enabled": True},
    {"_id": "lumina", "name": "LUMINA", "enabled": True},
]

DEFAULT_ECOMMERCE_CARDS = [
    {
        "_id": "visual-search-discovery",
        "title": "Visual Search & Discovery",
        "description": "AI-driven visual recognition allowing customers to find products using nothing but a single image capture.",
        "image_src": "/images/solutions_visual_search.png",
        "image_alt": "Blacksoft Visual Search Shoe Scan App",
        "is_placeholder": False,
        "enabled": True,
    },
    {
        "_id": "autonomous-shopping-agents",
        "title": "Autonomous Shopping Agents",
        "description": "Intelligent agents that manage procurement, negotiation, and scheduling for enterprise-scale B2B e-commerce.",
        "image_src": "",
        "image_alt": "Blacksoft Autonomous AI Shopping Agent",
        "is_placeholder": True,
        "enabled": True,
    },
    {
        "_id": "predictive-inventory-management",
        "title": "Predictive Inventory Management",
        "description": "Anticipate demand surges before they happen, optimizing logistics and reducing overhead by up to 40%.",
        "image_src": "/images/solutions_predictive_inventory.png",
        "image_alt": "Blacksoft Predictive Inventory Logistics Dashboard",
        "is_placeholder": False,
        "enabled": True,
    },
]

DEFAULT_TECH_STACK_CARDS = [
    # ── FIGMA ──────────────────────────────────────────────────────────────
    {
        "_id": "tech-figma",
        "title": "Figma",
        "category": "FIGMA",
        "description": "Industry-standard collaborative design tool for creating wireframes, UI systems, prototypes, and high-fidelity mockups in real time.",
        "icon_key": "design",
        "enabled": True,
    },
    {
        "_id": "tech-figma-variables",
        "title": "Figma Variables & Tokens",
        "category": "FIGMA",
        "description": "Design token system inside Figma enabling shared color, spacing, and typography scales across the entire product design system.",
        "icon_key": "design",
        "enabled": True,
    },
    {
        "_id": "tech-figma-auto-layout",
        "title": "Auto Layout & Components",
        "category": "FIGMA",
        "description": "Responsive component architecture with auto layout, nested variants, and interactive prototyping flows for pixel-perfect handoffs.",
        "icon_key": "design",
        "enabled": True,
    },
    {
        "_id": "tech-tailwind",
        "title": "Tailwind CSS",
        "category": "FIGMA",
        "description": "Utility-first CSS framework enabling rapid UI development with consistent design tokens — pairs perfectly with Figma design systems.",
        "icon_key": "design",
        "enabled": True,
    },
    # ── FRONTEND ───────────────────────────────────────────────────────────
    {
        "_id": "tech-react",
        "title": "React.js",
        "category": "FRONTEND",
        "description": "Component-based UI library powering fast, dynamic single-page apps with Virtual DOM and a massive ecosystem.",
        "icon_key": "frontend",
        "enabled": True,
    },
    {
        "_id": "tech-nextjs",
        "title": "Next.js",
        "category": "FRONTEND",
        "description": "Full-stack React framework with SSR, SSG, App Router, and edge-optimized rendering for SEO-heavy production web apps.",
        "icon_key": "frontend",
        "enabled": True,
    },
    {
        "_id": "tech-angular",
        "title": "Angular",
        "category": "FRONTEND",
        "description": "Complete MVC, TypeScript-native enterprise framework by Google for large-scale, rigid, structured applications.",
        "icon_key": "frontend",
        "enabled": True,
    },
    {
        "_id": "tech-vuejs",
        "title": "Vue.js",
        "category": "FRONTEND",
        "description": "Progressive reactive framework with an approachable Composition API and excellent performance for modern SPAs.",
        "icon_key": "frontend",
        "enabled": True,
    },
    {
        "_id": "tech-svelte",
        "title": "Svelte",
        "category": "FRONTEND",
        "description": "Compiler-first framework that ships zero-runtime JavaScript, producing ultra-fast lightweight web interfaces.",
        "icon_key": "frontend",
        "enabled": True,
    },
    {
        "_id": "tech-typescript",
        "title": "TypeScript",
        "category": "FRONTEND",
        "description": "Typed superset of JavaScript enabling large-scale codebases with autocompletion, refactoring, and compile-time safety.",
        "icon_key": "frontend",
        "enabled": True,
    },
    {
        "_id": "tech-vite",
        "title": "Vite",
        "category": "FRONTEND",
        "description": "Lightning-fast build tool using native ESM and Rollup, delivering sub-second HMR for modern frontend projects.",
        "icon_key": "devops",
        "enabled": True,
    },
    # ── APP ────────────────────────────────────────────────────────────────
    {
        "_id": "tech-react-native",
        "title": "React Native",
        "category": "APP",
        "description": "Best for JavaScript/Web Teams (Meta). Uses real platform-native components instead of a WebView, giving an authentic native feel. Extremely mature with Fabric architecture and widespread Expo adoption.",
        "icon_key": "mobile",
        "enabled": True,
    },
    {
        "_id": "tech-flutter",
        "title": "Flutter",
        "category": "APP",
        "description": "Best for Canvas Performance & Visual Fidelity (Google). Written in Dart, Flutter renders every pixel via the Impeller engine — bypassing native UI for exact cross-platform consistency and near-native speeds.",
        "icon_key": "mobile",
        "enabled": True,
    },
    {
        "_id": "tech-kotlin",
        "title": "Kotlin Multiplatform",
        "category": "APP",
        "description": "Best for Shared Logic with Native UI (JetBrains). Share business logic across iOS and Android while keeping platform-specific native UI for full native experience.",
        "icon_key": "mobile",
        "enabled": True,
    },
    {
        "_id": "tech-swift",
        "title": "Swift (iOS)",
        "category": "APP",
        "description": "Apple's fast, safe language for building high-performance native iOS, macOS, and iPadOS applications with full access to Apple platform APIs.",
        "icon_key": "mobile",
        "enabled": True,
    },
    {
        "_id": "tech-java",
        "title": "Java (Android)",
        "category": "APP",
        "description": "Mature JVM language for Android development with a broad library ecosystem, enterprise-grade stability, and full Android SDK compatibility.",
        "icon_key": "mobile",
        "enabled": True,
    },
    # ── BACKEND ────────────────────────────────────────────────────────────
    {
        "_id": "tech-nodejs",
        "title": "Node.js",
        "category": "BACKEND",
        "description": "Event-driven JavaScript runtime on V8 enabling high-concurrency APIs and microservices with non-blocking I/O.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-nestjs",
        "title": "NestJS",
        "category": "BACKEND",
        "description": "Scalable TypeScript Node framework with Angular-inspired modules, decorators, and built-in DI for enterprise APIs.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-express",
        "title": "Express.js",
        "category": "BACKEND",
        "description": "Minimal and flexible Node.js framework for building RESTful APIs and middleware-driven server applications.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-fastapi",
        "title": "FastAPI",
        "category": "BACKEND",
        "description": "High-performance Python async framework with auto OpenAPI docs, Pydantic validation, and blazing-fast I/O.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-django",
        "title": "Django",
        "category": "BACKEND",
        "description": "Batteries-included Python framework with ORM, admin panel, and security-first design for rapid backend delivery.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-spring-boot",
        "title": "Spring Boot",
        "category": "BACKEND",
        "description": "Java enterprise framework with auto-configuration, embedded servers, and production-ready microservice support.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-laravel",
        "title": "Laravel",
        "category": "BACKEND",
        "description": "Elegant PHP framework with expressive ORM, queue management, real-time broadcasting, and developer-first tooling.",
        "icon_key": "backend",
        "enabled": True,
    },
    {
        "_id": "tech-go-gin",
        "title": "Go / Gin",
        "category": "BACKEND",
        "description": "Statically compiled high-throughput HTTP framework in Go for building ultra-low-latency microservices and APIs.",
        "icon_key": "backend",
        "enabled": True,
    },
    # ── DEPLOYMENT ─────────────────────────────────────────────────────────
    {
        "_id": "tech-docker",
        "title": "Docker",
        "category": "DEPLOYMENT",
        "description": "Containerization platform for packaging applications with all dependencies into portable, reproducible environments.",
        "icon_key": "orchestration",
        "enabled": True,
    },
    {
        "_id": "tech-kubernetes",
        "title": "Kubernetes",
        "category": "DEPLOYMENT",
        "description": "Production-grade container orchestration with auto-scaling, self-healing, and zero-downtime rolling deployments.",
        "icon_key": "orchestration",
        "enabled": True,
    },
    {
        "_id": "tech-aws",
        "title": "AWS",
        "category": "DEPLOYMENT",
        "description": "World's leading cloud platform with 200+ services for compute, storage, AI, and global-scale infrastructure.",
        "icon_key": "cloud",
        "enabled": True,
    },
    {
        "_id": "tech-gcp",
        "title": "Google Cloud",
        "category": "DEPLOYMENT",
        "description": "Google's cloud platform with first-class AI/ML tooling, BigQuery analytics, and globally distributed compute nodes.",
        "icon_key": "cloud",
        "enabled": True,
    },
    {
        "_id": "tech-vercel",
        "title": "Vercel",
        "category": "DEPLOYMENT",
        "description": "Frontend cloud platform with edge functions, preview deployments, and zero-config Next.js hosting at scale.",
        "icon_key": "cloud",
        "enabled": True,
    },
    {
        "_id": "tech-github-actions",
        "title": "GitHub Actions",
        "category": "DEPLOYMENT",
        "description": "CI/CD automation integrated in GitHub — test, build, and deploy on every push with reusable workflows.",
        "icon_key": "devops",
        "enabled": True,
    },
]

DEFAULT_APP_WEBSITE_CARDS = [
    {"_id": "web-product-builds", "title": "Product websites", "category": "Website", "description": "High-performance marketing sites and product surfaces that make complex technology easy to understand and use.", "icon": "WEB", "link": "#app-websites", "enabled": True},
    {"_id": "web-client-portals", "title": "Client portals", "category": "App", "description": "Secure, responsive workspaces that bring customers, data, and operational workflows into one clear experience.", "icon": "UX", "link": "#app-websites", "enabled": True},
    {"_id": "web-saas-platforms", "title": "SaaS platforms", "category": "App", "description": "Scalable application foundations with thoughtful onboarding, dashboards, permissions, and billing-ready architecture.", "icon": "APP", "link": "#app-websites", "enabled": True},
]

DEFAULT_AI_SOLUTION_CARDS = [
    {"_id": "ai-agents", "title": "AI agents", "category": "AI Solution", "description": "Goal-oriented agents that reason across tools, knowledge, and business rules to move work forward autonomously.", "icon": "AG", "link": "#ai-solutions", "enabled": True},
    {"_id": "ai-knowledge", "title": "Knowledge systems", "category": "AI Solution", "description": "Grounded search and retrieval systems that turn company knowledge into fast, trusted answers and actions.", "icon": "KN", "link": "#ai-solutions", "enabled": True},
    {"_id": "ai-automation", "title": "Intelligent automation", "category": "AI Solution", "description": "Connected workflows that remove repetitive work while keeping people in control of important decisions.", "icon": "AU", "link": "#ai-solutions", "enabled": True},
]

DEFAULT_TECH_STACK_SETTINGS = {
    "_id": "technology_stack",
    "section_title": "Our Technology Stack",
    "section_subtitle": "Built on battle-tested frameworks and advanced cloud kernels.",
}

DEFAULT_TEAM_MEMBERS = []

DEFAULT_TEAM_SETTINGS = {
    "_id": "team_members",
    "title": "The Architects",
    "subtitle": "A team of visionaries, engineers, and researchers dedicated to the pursuit of super-intelligence.",
    "cta_label": "Full Team History",
    "cta_link": "#careers",
}


DEFAULT_SERVICES = [
    {
        "_id": "ai-first-systems",
        "title": "AI-First Architectures",
        "description": "Custom agentic systems, context-aware LLMs, and intelligent automation pipelines built to handle sophisticated cognitive tasks.",
        "icon": "🧠",
        "enabled": True,
    },
    {
        "_id": "next-gen-web",
        "title": "Next-Gen Web Platforms",
        "description": "High-fidelity, responsive, and server-rendered web systems designed for lightning-fast speeds and premium user interaction.",
        "icon": "🌐",
        "enabled": True,
    },
    {
        "_id": "mobile-solutions",
        "title": "Native & Mobile Solutions",
        "description": "Fluid, high-performance applications built for iOS and Android, focusing on modern aesthetics and optimized response times.",
        "icon": "📱",
        "enabled": True,
    },
    {
        "_id": "interactive-design",
        "title": "Interactive Product Design",
        "description": "Crafting premium user journeys, dynamic wireframes, and design blueprints structured around user experience clarity.",
        "icon": "🎨",
        "enabled": True,
    },
    {
        "_id": "brand-identity",
        "title": "Brand Strategy & Systems",
        "description": "Formulating complete visual languages, brand typography, vector assets, and design libraries to build a memorable identity.",
        "icon": "✨",
        "enabled": True,
    },
]


DEFAULT_WHO_WE_ARE_SETTINGS = {
    "_id": "who_we_are",
    "tag": "WHO WE ARE",
    "title": "We are a collective of digital engineers, designers, and systems architects.",
    "description": "At Blacksoft, we build high-fidelity software products, autonomous agent layers, and scalable cloud infrastructure for startups and modern companies.",
    "highlight1Num": "50+",
    "highlight1Label": "Intelligent Systems Shipped",
    "highlight2Num": "99.9%",
    "highlight2Label": "SLA System Availability",
    "highlight3Num": "24/7",
    "highlight3Label": "Continuous Optimization",
}


DEFAULT_WHY_US = [
    {
        "_id": "ai-native-exec",
        "title": "AI-Native Execution",
        "description": "We build software with modern LLM backbones, enabling rapid code generation and highly adaptive logic paths.",
        "icon": "⚡",
        "enabled": True,
    },
    {
        "_id": "enterprise-sec",
        "title": "Enterprise Security",
        "description": "Built on zero-trust principles, SOC 2 alignment, and strict data boundary configurations to keep your assets safe.",
        "icon": "🔒",
        "enabled": True,
    },
    {
        "_id": "absolute-scale",
        "title": "Absolute Scalability",
        "description": "Designed to handle high request concurrency and massive user spikes with containerized compute nodes.",
        "icon": "🚀",
        "enabled": True,
    },
    {
        "_id": "collab-partners",
        "title": "Collaborative Partners",
        "description": "We work closely with your internal teams, transferring all product knowledge and code ownership smoothly.",
        "icon": "🤝",
        "enabled": True,
    },
]


async def seed_dashboard_content() -> None:
    db = get_db()

    # Ensure services list updates to the new premium names
    await db.services.delete_many({})
    await db.services.insert_many(DEFAULT_SERVICES)

    # Ensure why us list updates to the new defaults
    await db.why_us.delete_many({})
    await db.why_us.insert_many(DEFAULT_WHY_US)

    # Collections that only seed when empty (insert-once)
    insert_once_seeds = [
        ("capabilities", DEFAULT_CAPABILITIES),
        ("innovators", DEFAULT_INNOVATORS),
        ("ecommerce_cards", DEFAULT_ECOMMERCE_CARDS),
        ("app_website_cards", DEFAULT_APP_WEBSITE_CARDS),
        ("ai_solution_cards", DEFAULT_AI_SOLUTION_CARDS),
        ("team_members", DEFAULT_TEAM_MEMBERS),
    ]

    for collection_name, documents in insert_once_seeds:
        collection = getattr(db, collection_name)
        if await collection.count_documents({}) == 0 and documents:
            await collection.insert_many(documents)

    # Technology stack cards: always upsert so new cards are added on redeploy
    # without removing cards the user has added via the dashboard.
    tech_collection = db.technology_stack_cards
    for card in DEFAULT_TECH_STACK_CARDS:
        await tech_collection.update_one(
            {"_id": card["_id"]},
            {"$setOnInsert": card},
            upsert=True,
        )

    settings_seeds = [
        ("technology_stack_settings", DEFAULT_TECH_STACK_SETTINGS),
        ("team_settings", DEFAULT_TEAM_SETTINGS),
        ("who_we_are_settings", DEFAULT_WHO_WE_ARE_SETTINGS),
    ]

    for collection_name, document in settings_seeds:
        collection = getattr(db, collection_name)
        if await collection.count_documents({}) == 0:
            await collection.insert_one(document)

