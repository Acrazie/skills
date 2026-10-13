import type { Locale } from './ui';

export interface LocalizedSkillMeta {
  category?: string;
  description?: string;
}

export const CATEGORY_TRANSLATIONS: Record<string, Record<Locale, string>> = {
  'CI/CD & DevOps': {
    en: 'CI/CD & DevOps',
    fr: 'CI/CD & DevOps',
    zh: 'CI/CD 与 DevOps',
  },
  'Design & Visuals': {
    en: 'Design & Visuals',
    fr: 'Design & Visuels',
    zh: '设计与视觉',
  },
  'Repository & Governance': {
    en: 'Repository & Governance',
    fr: 'Dépôt & Gouvernance',
    zh: '仓库与治理',
  },
  'Architecture & Review': {
    en: 'Architecture & Review',
    fr: 'Architecture & Revue',
    zh: '架构与审查',
  },
  'Agent & DX Tools': {
    en: 'Agent & DX Tools',
    fr: 'Outils Agent & DX',
    zh: 'Agent 与 DX 工具',
  },
};

export const SKILL_METADATA_TRANSLATIONS: Record<string, Record<Locale, LocalizedSkillMeta>> = {
  'audit-repository-acrazie': {
    en: {
      description: 'Audit a precise technical decision, integration, tool, stack choice, or subsystem in one existing repository. Use when the task needs a bounded technical assessment before a decision, including read-only selected-script portability assessment and a separately authorized executor handoff; not for general repository audits, diff or PR review, security audits, documentation audits, or multi-repository analysis.',
    },
    fr: {
      description: 'Auditer une décision technique précise, une intégration, un outil, un choix de stack ou un sous-système dans un dépôt existant. Pour une évaluation technique ciblée nécessaire à la décision demandée, y compris portabilité de scripts sélectionnés en lecture seule et transmission à un exécutant séparément autorisé.',
    },
    zh: {
      description: '针对现有代码库中的具体技术决策、工具集成、技术栈选型或子系统进行针对性审计。适用于当前任务所需的针对性技术评估，包括选定脚本可移植性的只读评估及另行授权的执行交接。',
    },
  },
  'canvas-banner-designer-acrazie': {
    en: {
      description: 'Design and implement animated HTML Canvas banners, web heroes, and ambient backgrounds with purposeful mouse interaction. Use when the user wants a living landscape, procedural scene, interactive line field, atmospheric backdrop, or generative header delivered as standalone HTML or a component in an existing web project. Not for Canva documents, static SVG/social cards, whole-site redesigns, or scroll-only animation.',
    },
    fr: {
      description: 'Concevoir et implémenter des bannières HTML Canvas animées, des en-têtes web et des arrière-plans réactifs à la souris. Idéal pour scènes génératives ou procédurales autonomes ou intégrées.',
    },
    zh: {
      description: '设计并实现具备鼠标交互响应的 HTML Canvas 动态横幅、Hero 模块与环境背景。适用于生成式风景、程序化线条网络与交互式氛围画布。',
    },
  },
  'git-ship-acrazie': {
    en: {
      description: 'Finalize, commit, push, and open Pull Requests for completed tasks based on repository Git rules and governance. Use when the user asks to ship changes, commit completed work, publish a branch, or create a draft PR; not merely because implementation is complete.',
    },
    fr: {
      description: 'Finaliser, commiter, pousser et ouvrir des Pull Requests pour des tâches terminées selon les règles Git et la gouvernance du dépôt. À invoquer pour expédier des modifications ou publier une branche.',
    },
    zh: {
      description: '严格遵循仓库 Git 规则与治理规范，完成代码提交、分支推送并自动发起 Pull Request。用于发布已完成变更或推送审查分支。',
    },
  },
  'github-repo-init-acrazie': {
    en: {
      description: 'Initialize repositories, activate an approved project-local engineering kit, or administer GitHub.com repository settings and personal Developer Settings (GitHub Apps, OAuth Apps, PATs). Discover read-only; every mutation requires prior approval. Includes verified automation and guided manual steps, not organization-wide administration, Enterprise Server, Git shipping or deployment.',
    },
    fr: {
      description: 'Initialiser un dépôt, activer un kit engineering local approuvé ou administrer les paramètres des dépôts GitHub.com et les Developer Settings personnels (GitHub Apps, OAuth Apps, PAT). Découverte en lecture seule ; toute modification nécessite une validation préalable. Automatisation vérifiée ou étapes manuelles guidées, sans administration globale des organisations, Enterprise Server, livraison Git ni déploiement.',
    },
    zh: {
      description: '初始化仓库、启用经批准的项目本地工程技能包，或管理 GitHub.com 仓库设置和个人 Developer Settings（GitHub Apps、OAuth Apps、PAT）。仅允许只读发现；任何修改都须事先批准。提供经过验证的自动化或人工操作指引，不包括组织级管理、Enterprise Server、Git 发布或部署。',
    },
  },
  'immersive-hero-designer-acrazie': {
    en: {
      description: 'Design and build an original, complete immersive web hero using the right medium for the effect: supplied or approved video, image sequence, 3D, Canvas, or CSS. Use when the user requests a cinematic, interactive, or scroll-driven section in an existing site; not for copying a reference, redesigning a whole site, or making a standalone video without a web hero.',
    },
    fr: {
      description: 'Concevoir et réaliser une section hero immersive originale (vidéo, séquence d’images, 3D, Canvas ou CSS). À invoquer pour créer une section cinématique ou interactive.',
    },
    zh: {
      description: '运用视频、图像序列、3D、Canvas 或 CSS 设计并构建引人入胜的沉浸式网页 Hero 模块。用于创建具有电影质感或交互动效的网页视觉模块。',
    },
  },
  'ci-cd-acrazie': {
    en: {
      description: 'Design, modernize and diagnose repository CI/CD across tools and languages. Runs, publication, promotion, deployment and rollback require separate authorization. Not platform or cloud administration.',
    },
    fr: {
      description: 'Concevoir, moderniser et diagnostiquer la CI/CD du dépôt, indépendamment du langage et de l’outil. Exécution, publication, promotion, déploiement et rollback sous autorisations distinctes. Hors administration plateformes/cloud.',
    },
    zh: {
      description: '跨语言与工具设计、现代化和诊断仓库 CI/CD。运行、发布、晋级、部署及回滚须分别授权。不负责平台或云基础设施管理。',
    },
  },
  'multi-agent-planner-acrazie': {
    en: {
      description: 'Decide single-agent vs multi-agent execution through a short option-driven interview and produce a verified copy-paste workflow. Use when the user asks to plan agent execution, compare single-agent and multi-agent approaches, or partition a task for agents; not merely because a task is large or spans repositories. Never for execution itself.',
    },
    fr: {
      description: 'Arbitrer entre exécution mono-agent et multi-agents via un court entretien, et produire un workflow prêt à copier-coller. Pour une demande de planification d’agents ; ni entretien imposé sur une tâche d’implémentation, ni lancement d’agents.',
    },
    zh: {
      description: '通过选项驱动问询评估单 Agent 与多 Agent 协作方案，生成经过验证的执行工作流。仅用于用户要求的 Agent 执行规划，不因任务复杂而自动启动，也不启动子 Agent。',
    },
  },
  'repo-modernizer-acrazie': {
    en: {
      description: 'Audit an existing repository setup, identify outdated tools, frameworks, and runtimes, and guide safe, step-by-step modernizations, upgrades, and paradigm shifts across 6 thematic pillars. Use when the user requests upgrades or modernization of an existing repository; not for opportunistic modernization during another task, greenfield scaffolding, or general code reviews.',
    },
    fr: {
      description: 'Auditer la configuration d’un dépôt existant, identifier les outils et frameworks obsolètes, et guider des modernisations progressives et sécurisées selon 6 piliers thématiques.',
    },
    zh: {
      description: '审计现有仓库架构，识别陈旧的工具链、框架与运行时，依循 6 大核心支柱稳步推进安全现代化演进与技术升级。',
    },
  },
  'repository-readme-architect-acrazie': {
    en: {
      description: 'Design, create, restructure, or update the primary README of a software repository through repository inspection, an adaptive decision-tree interview, architecture options, and an approval-gated edit. Use for the repository README, not generic Markdown documentation or ancillary files.',
    },
    fr: {
      description: 'Concevoir, structurer ou moderniser le README principal d’un dépôt logiciel après inspection, entretien adaptatif et validation explicite d’architecture.',
    },
    zh: {
      description: '通过深度代码库探索与自适应决策树问询，设计、重构并编写软件仓库权威主 README 文档。',
    },
  },
  'skill-refiner-acrazie': {
    en: {
      description: 'Collect structured feedback while a user tests one target skill, preserve observations in an append-only journal, and consolidate approved feedback into a behavior record, with ADRs only for durable nontrivial trade-offs. Use only when the user explicitly invokes skill-refiner-acrazie for an interactive refinement campaign; do not edit the target skill.',
    },
    fr: {
      description: 'Recueillir des retours structurés lors du test d’un skill cible, consigner les observations dans un journal immuable et consolider les retours validés dans un registre comportemental ; réserver les ADR aux arbitrages durables non triviaux. Activation explicite uniquement ; ne modifie pas le skill cible.',
    },
    zh: {
      description: '在用户测试一个目标技能时收集结构化反馈，以追加式日志保留观察，并在行为记录中汇总经批准的反馈；仅将长期且非平凡的权衡写入 ADR。仅显式启用，不修改目标技能。',
    },
  },
  'svg-designer-acrazie': {
    en: {
      description: 'Design original static SVG icons, logos, banners, social cards and header graphics with target-specific checks and only approved raster or favicon exports. Not raster image editing, animated scenes, whole-site UI redesign or general diagramming.',
    },
    fr: {
      description: 'Concevoir des icônes, logos, bannières, social cards et en-têtes SVG statiques originaux, avec vérifications adaptées à la cible et seuls exports raster ou favicon approuvés. Hors retouche raster, scènes animées, refonte complète d’interface et diagrammes génériques.',
    },
    zh: {
      description: '设计原创静态 SVG 图标、标志、横幅、社交预览卡与页头图形，按实际用途验证，并仅导出获准的位图或 Favicon。不用于位图编辑、动画场景、整站界面重设计或通用图表。',
    },
  },
};

export function getLocalizedSkillMeta(id: string, lang: Locale, fallbackCategory: string, fallbackDescription: string): { category: string; description: string } {
  const meta = SKILL_METADATA_TRANSLATIONS[id]?.[lang];
  const translatedCategory = CATEGORY_TRANSLATIONS[fallbackCategory]?.[lang] ?? fallbackCategory;
  const translatedDescription = meta?.description || fallbackDescription;

  return {
    category: translatedCategory,
    description: translatedDescription,
  };
}
