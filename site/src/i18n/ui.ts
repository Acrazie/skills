export type Locale = 'en' | 'fr' | 'zh';

export const LOCALES: Record<Locale, { label: string; flag: string; htmlLang: string }> = {
  en: { label: 'English', flag: 'EN', htmlLang: 'en' },
  fr: { label: 'Français', flag: 'FR', htmlLang: 'fr' },
  zh: { label: '简体中文', flag: 'ZH', htmlLang: 'zh-CN' },
};

export const DEFAULT_LOCALE: Locale = 'en';

export const UI_TRANSLATIONS = {
  en: {
    // Header & Navigation
    'nav.brandAria': 'Acrazie Skills, home',
    'nav.catalogue': 'Catalogue',
    'nav.changelog': 'Changelog',
    'nav.skillsSh': 'skills.sh',
    'nav.skillsShAria': 'skills.sh documentation registry',
    'nav.githubAria': 'Acrazie Skills GitHub repository',
    'nav.selectLang': 'Select language',
    'copy.title': 'Copy to clipboard',
    'copy.success': 'Command copied',
    'copy.error': 'Could not copy. Select the command manually.',

    // Hero
    'hero.title': 'Precision skills for AI coding agents.',
    'hero.description': 'Explore specialized workflows, review their instructions, and install only what your agent needs.',
    'hero.copyPrompt': 'Copy command',
    'hero.copied': 'Copied!',
    'hero.explore': 'Explore catalogue',
    'hero.pause': 'Pause animation',
    'hero.resume': 'Resume animation',
    'hero.pauseAction': 'Pause',
    'hero.resumeAction': 'Resume',

    // Catalogue
    'catalogue.title': 'Find the right skill.',
    'catalogue.subtitle': 'Browse workflows, inspect their instructions, and copy the installation command.',
    'catalogue.skillsCount': (n: number) => `${n} skill${n === 1 ? '' : 's'}`,
    'catalogue.searchLabel': 'Search for a skill',
    'catalogue.searchPlaceholder': 'Search for a skill or workflow…',
    'catalogue.allCategories': 'All',
    'catalogue.columnsSkill': 'Skill',
    'catalogue.columnsDescription': 'Description',
    'catalogue.columnsCategory': 'Category',
    'catalogue.emptyTitle': 'No skills found',
    'catalogue.emptyDesc': 'Try another keyword or select another category.',
    'catalogue.resetFilters': 'Reset filters',

    // Skill Card
    'card.userInvoked': 'User invocation',
    'card.copyInstallAria': (id: string) => `Copy install command for ${id}`,
    'card.detailsAria': (id: string) => `View instructions for ${id}`,

    // Skill Detail Page
    'detail.backToCatalogue': 'Back to catalogue',
    'detail.userInvoked': 'User Invocation Only',
    'detail.implicitAndExplicit': 'Implicit & Explicit',
    'detail.copyCommand': 'Copy command',
    'detail.copied': 'Copied!',
    'detail.onThisPage': 'On this page',
    'detail.instructions': 'Instructions',
    'detail.references': 'References',
    'detail.referencesIntro': 'Domain guides, checklists, and references bundled with this skill.',
    'detail.viewOnGithub': 'View on GitHub',

    // Changelog
    'changelog.title': 'Changelog',
    'changelog.subtitle': 'Release history and evolutions of the Acrazie Skills monorepo.',
    'changelog.releasesLink': 'GitHub Releases',
    'changelog.backToCatalogue': 'Back to catalogue',

    // Footer
    'footer.tagline': 'Specialized workflows for AI coding agents.',
    'footer.catalogue': 'Catalogue',
    'footer.changelog': 'Changelog',

    // Metadata
    'meta.siteTitle': 'Acrazie Skills — Agent skills for AI coding agents',
    'meta.siteDescription': 'Discover, inspect, and install precision workflows for AI coding agents published to skills.sh.',
    'meta.changelogTitle': 'Changelog — Acrazie Skills',
    'meta.changelogDescription': 'Release history and evolutions of the Acrazie Skills monorepo.',
  },
  fr: {
    // Header & Navigation
    'nav.brandAria': 'Acrazie Skills, accueil',
    'nav.catalogue': 'Catalogue',
    'nav.changelog': 'Changelog',
    'nav.skillsSh': 'skills.sh',
    'nav.skillsShAria': 'Documentation sur skills.sh',
    'nav.githubAria': 'Dépôt GitHub Acrazie Skills',
    'nav.selectLang': 'Changer de langue',
    'copy.title': 'Copier dans le presse-papiers',
    'copy.success': 'Commande copiée',
    'copy.error': 'Copie impossible. Sélectionnez la commande manuellement.',

    // Hero
    'hero.title': 'Des skills précis pour vos agents de code.',
    'hero.description': 'Explorez des workflows spécialisés, lisez leurs instructions et installez ceux dont votre agent a besoin.',
    'hero.copyPrompt': 'Copier',
    'hero.copied': 'Copié !',
    'hero.explore': 'Explorer le catalogue',
    'hero.pause': 'Mettre l’animation en pause',
    'hero.resume': 'Reprendre l’animation',
    'hero.pauseAction': 'Pause',
    'hero.resumeAction': 'Reprendre',

    // Catalogue
    'catalogue.title': 'Trouvez le bon skill.',
    'catalogue.subtitle': 'Parcourez les workflows, consultez leurs instructions, puis copiez la commande d\'installation.',
    'catalogue.skillsCount': (n: number) => `${n} skill${n === 1 ? '' : 's'}`,
    'catalogue.searchLabel': 'Rechercher un skill',
    'catalogue.searchPlaceholder': 'Rechercher un skill ou un workflow…',
    'catalogue.allCategories': 'Tout',
    'catalogue.columnsSkill': 'Skill',
    'catalogue.columnsDescription': 'Description',
    'catalogue.columnsCategory': 'Catégorie',
    'catalogue.emptyTitle': 'Aucun skill trouvé',
    'catalogue.emptyDesc': 'Essayez un autre terme ou une autre catégorie.',
    'catalogue.resetFilters': 'Réinitialiser les filtres',

    // Skill Card
    'card.userInvoked': 'Sur invocation',
    'card.copyInstallAria': (id: string) => `Copier la commande d’installation de ${id}`,
    'card.detailsAria': (id: string) => `Voir les instructions de ${id}`,

    // Skill Detail Page
    'detail.backToCatalogue': 'Retour au catalogue',
    'detail.userInvoked': 'Sur invocation explicite',
    'detail.implicitAndExplicit': 'Implicite & Explicite',
    'detail.copyCommand': 'Copier la commande',
    'detail.copied': 'Copié !',
    'detail.onThisPage': 'Sur cette page',
    'detail.instructions': 'Instructions',
    'detail.references': 'Références',
    'detail.referencesIntro': 'Guides et ressources inclus avec ce skill.',
    'detail.viewOnGithub': 'Voir sur GitHub',

    // Changelog
    'changelog.title': 'Changelog',
    'changelog.subtitle': 'Évolutions du monorepo Acrazie Skills.',
    'changelog.releasesLink': 'Releases GitHub',
    'changelog.backToCatalogue': 'Retour au catalogue',

    // Footer
    'footer.tagline': 'Workflows spécialisés pour agents de code.',
    'footer.catalogue': 'Catalogue',
    'footer.changelog': 'Changelog',

    // Metadata
    'meta.siteTitle': 'Acrazie Skills — Skills pour agents de code',
    'meta.siteDescription': 'Découvrez, consultez et installez des skills spécialisés pour agents de code.',
    'meta.changelogTitle': 'Changelog — Acrazie Skills',
    'meta.changelogDescription': 'Historique des versions du monorepo Acrazie Skills.',
  },
  zh: {
    // Header & Navigation
    'nav.brandAria': 'Acrazie Skills 首页',
    'nav.catalogue': '目录',
    'nav.changelog': '更新日志',
    'nav.skillsSh': 'skills.sh',
    'nav.skillsShAria': 'skills.sh 文档注册中心',
    'nav.githubAria': 'Acrazie Skills GitHub 仓库',
    'nav.selectLang': '选择语言',
    'copy.title': '复制到剪贴板',
    'copy.success': '命令已复制',
    'copy.error': '无法复制。请手动选择命令。',

    // Hero
    'hero.title': '面向 AI 编程 Agent 的高精度技能。',
    'hero.description': '探索专属工作流，查阅规范指令，一键安装 Agent 所需技能。',
    'hero.copyPrompt': '复制',
    'hero.copied': '已复制！',
    'hero.explore': '浏览目录',
    'hero.pause': '暂停动画',
    'hero.resume': '恢复动画',
    'hero.pauseAction': '暂停',
    'hero.resumeAction': '继续',

    // Catalogue
    'catalogue.title': '查找合适的技能。',
    'catalogue.subtitle': '浏览精选工作流，检查执行指令，快速复制安装命令。',
    'catalogue.skillsCount': (n: number) => `${n} 个技能`,
    'catalogue.searchLabel': '搜索技能',
    'catalogue.searchPlaceholder': '搜索技能或工作流…',
    'catalogue.allCategories': '全部',
    'catalogue.columnsSkill': '技能',
    'catalogue.columnsDescription': '描述',
    'catalogue.columnsCategory': '分类',
    'catalogue.emptyTitle': '未找到相关技能',
    'catalogue.emptyDesc': '请尝试使用其他关键词或切换分类。',
    'catalogue.resetFilters': '重置筛选条件',

    // Skill Card
    'card.userInvoked': '仅限显式调用',
    'card.copyInstallAria': (id: string) => `复制 ${id} 的安装命令`,
    'card.detailsAria': (id: string) => `查看 ${id} 的详细说明`,

    // Skill Detail Page
    'detail.backToCatalogue': '返回目录',
    'detail.userInvoked': '仅限用户显式调用',
    'detail.implicitAndExplicit': '隐式与显式均支持',
    'detail.copyCommand': '复制命令',
    'detail.copied': '已复制！',
    'detail.onThisPage': '本页导航',
    'detail.instructions': '指令规范',
    'detail.references': '参考指南',
    'detail.referencesIntro': '随附该技能提供的领域指南与清单文档。',
    'detail.viewOnGithub': '在 GitHub 上查看',

    // Changelog
    'changelog.title': '更新日志',
    'changelog.subtitle': 'Acrazie Skills 单体仓库的版本演化历史与更新记录。',
    'changelog.releasesLink': 'GitHub 发行版',
    'changelog.backToCatalogue': '返回目录',

    // Footer
    'footer.tagline': '面向 AI 编程 Agent 的专属自动化工作流。',
    'footer.catalogue': '目录',
    'footer.changelog': '更新日志',

    // Metadata
    'meta.siteTitle': 'Acrazie Skills — AI 编程 Agent 专属技能库',
    'meta.siteDescription': '发现、查阅并安装发布于 skills.sh 的 AI 编程 Agent 高精度工作流技能。',
    'meta.changelogTitle': '更新日志 — Acrazie Skills',
    'meta.changelogDescription': 'Acrazie Skills 单体仓库版本发布历史。',
  },
} as const;

export type TranslationKey = keyof typeof UI_TRANSLATIONS['en'];

export function getLangFromUrl(url: URL | string): Locale {
  const pathname = typeof url === 'string' ? url : url.pathname;
  const segments = pathname.split('/').filter(Boolean);
  const first = segments[0];
  if (first === 'fr') return 'fr';
  if (first === 'zh') return 'zh';
  return 'en';
}

export function useTranslations(lang: Locale) {
  const dict = UI_TRANSLATIONS[lang] || UI_TRANSLATIONS.en;
  return function t<K extends TranslationKey>(key: K): (typeof UI_TRANSLATIONS['en'])[K] {
    return (dict as any)[key] ?? (UI_TRANSLATIONS.en as any)[key];
  };
}

export function getLocalizedPath(pathname: string, targetLang: Locale): string {
  let clean = pathname.startsWith('/') ? pathname : `/${pathname}`;

  // Remove existing locale prefix (/fr/ or /zh/)
  if (clean.startsWith('/fr/')) {
    clean = clean.slice(3);
  } else if (clean === '/fr') {
    clean = '/';
  } else if (clean.startsWith('/zh/')) {
    clean = clean.slice(3);
  } else if (clean === '/zh') {
    clean = '/';
  }

  // Ensure trailing slash for non-empty paths
  if (clean !== '/' && !clean.endsWith('/')) {
    clean = `${clean}/`;
  }

  if (targetLang === 'en') {
    return clean;
  }

  return clean === '/' ? `/${targetLang}/` : `/${targetLang}${clean}`;
}
