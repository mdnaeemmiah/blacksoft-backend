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

DEFAULT_TECH_STACK_CARDS = [
    {
        "_id": "stack-card-1",
        "title": "PyTorch & TensorFlow",
        "category": "DEEP LEARNING PLATFORMS",
        "description": "Custom neural kernels, transformer backbones, and specialized gradient optimization paths.",
        "icon_key": "growth",
        "enabled": True,
    },
    {
        "_id": "stack-card-2",
        "title": "NVIDIA H100 Tensor Core",
        "category": "ACCELERATED HARDWARE",
        "description": "Distributed matrix computation pipelines with sub-millisecond node-to-node transfer speeds.",
        "icon_key": "hardware",
        "enabled": True,
    },
    {
        "_id": "stack-card-3",
        "title": "Kubernetes & Docker",
        "category": "ORCHESTRATION & CONTAINERIZATION",
        "description": "Dynamic pod autoscaling, zero-downtime rolling updates, and fully isolated model container runtime envs.",
        "icon_key": "orchestration",
        "enabled": True,
    },
    {
        "_id": "stack-card-4",
        "title": "Next.js & React Server Components",
        "category": "FRONTEND COMPILATION FRAMEWORKS",
        "description": "Statically prerendered enterprise interfaces, lightning-fast edge streaming, and type-safe backend schemas.",
        "icon_key": "frontend",
        "enabled": True,
    },
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

    seeds = [
        ("capabilities", DEFAULT_CAPABILITIES),
        ("innovators", DEFAULT_INNOVATORS),
        ("ecommerce_cards", DEFAULT_ECOMMERCE_CARDS),
        ("app_website_cards", DEFAULT_APP_WEBSITE_CARDS),
        ("ai_solution_cards", DEFAULT_AI_SOLUTION_CARDS),
        ("technology_stack_cards", DEFAULT_TECH_STACK_CARDS),
        ("team_members", DEFAULT_TEAM_MEMBERS),
    ]

    for collection_name, documents in seeds:
        collection = getattr(db, collection_name)
        if await collection.count_documents({}) == 0 and documents:
            await collection.insert_many(documents)

    settings_seeds = [
        ("technology_stack_settings", DEFAULT_TECH_STACK_SETTINGS),
        ("team_settings", DEFAULT_TEAM_SETTINGS),
        ("who_we_are_settings", DEFAULT_WHO_WE_ARE_SETTINGS),
    ]

    for collection_name, document in settings_seeds:
        collection = getattr(db, collection_name)
        if await collection.count_documents({}) == 0:
            await collection.insert_one(document)
