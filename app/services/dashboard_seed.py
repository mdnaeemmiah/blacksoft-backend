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
    {"_id": "web-product-builds", "title": "Product websites", "description": "High-performance marketing sites and product surfaces that make complex technology easy to understand and use.", "icon": "WEB", "link": "#app-websites", "enabled": True},
    {"_id": "web-client-portals", "title": "Client portals", "description": "Secure, responsive workspaces that bring customers, data, and operational workflows into one clear experience.", "icon": "UX", "link": "#app-websites", "enabled": True},
    {"_id": "web-saas-platforms", "title": "SaaS platforms", "description": "Scalable application foundations with thoughtful onboarding, dashboards, permissions, and billing-ready architecture.", "icon": "APP", "link": "#app-websites", "enabled": True},
]

DEFAULT_AI_SOLUTION_CARDS = [
    {"_id": "ai-agents", "title": "AI agents", "description": "Goal-oriented agents that reason across tools, knowledge, and business rules to move work forward autonomously.", "icon": "AG", "link": "#ai-solutions", "enabled": True},
    {"_id": "ai-knowledge", "title": "Knowledge systems", "description": "Grounded search and retrieval systems that turn company knowledge into fast, trusted answers and actions.", "icon": "KN", "link": "#ai-solutions", "enabled": True},
    {"_id": "ai-automation", "title": "Intelligent automation", "description": "Connected workflows that remove repetitive work while keeping people in control of important decisions.", "icon": "AU", "link": "#ai-solutions", "enabled": True},
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

DEFAULT_TEAM_MEMBERS = [
    {
        "_id": "team-member-1",
        "name": "Dr. Elena Vance",
        "role": "CHIEF SCIENTIST & FOUNDER",
        "image_src": "/images/team_elena.png",
        "image_alt": "Dr. Elena Vance - Chief Scientist & Founder at Blacksoft",
        "enabled": True,
    },
    {
        "_id": "team-member-2",
        "name": "Marcus Thorne",
        "role": "HEAD OF ENGINEERING",
        "image_src": "/images/team_marcus.png",
        "image_alt": "Marcus Thorne - Head of Engineering at Blacksoft",
        "enabled": True,
    },
    {
        "_id": "team-member-3",
        "name": "Sarah Chen",
        "role": "VP OF STRATEGY",
        "image_src": "/images/team_sarah.png",
        "image_alt": "Sarah Chen - VP of Strategy at Blacksoft",
        "enabled": True,
    },
    {
        "_id": "team-member-4",
        "name": "Julian Kross",
        "role": "LEAD NEURAL ARCHITECT",
        "image_src": "/images/team_julian.png",
        "image_alt": "Julian Kross - Lead Neural Architect at Blacksoft",
        "enabled": True,
    },
]

DEFAULT_TEAM_SETTINGS = {
    "_id": "team_members",
    "title": "The Architects",
    "subtitle": "A team of visionaries, engineers, and researchers dedicated to the pursuit of super-intelligence.",
    "cta_label": "Full Team History",
    "cta_link": "#careers",
}


async def seed_dashboard_content() -> None:
    db = get_db()
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
        if await collection.count_documents({}) == 0:
            await collection.insert_many(documents)

    settings_seeds = [
        ("technology_stack_settings", DEFAULT_TECH_STACK_SETTINGS),
        ("team_settings", DEFAULT_TEAM_SETTINGS),
    ]

    for collection_name, document in settings_seeds:
        collection = getattr(db, collection_name)
        if await collection.count_documents({}) == 0:
            await collection.insert_one(document)
