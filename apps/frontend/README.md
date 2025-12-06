# Bun Vite React TypeScript Template

A starter template for React projects. Pre-configured with Bun, Vite, TypeScript, ESLint, and Prettier.
Clone it and start building.

## Disclaimer

This is opinionated. Use what works for you, ignore the rest, and stay consistent with your own choices.

## What's Included

### Core Stack

- **Bun** runtime and package manager
- **React 19** with **Vite** for fast development
- **TypeScript** for type safety
- **Tailwind CSS** for styling

### Testing

- **Bun Test** for unit and integration tests
- **React Testing Library** for component testing
- **happy-dom** for browser environment simulation

### Architecture

- Organized folder structure (`app`, `features`, `components`)
- Path aliases (`@/*` → `src/*`)
- VS Code auto-format on save

### Code Quality

- **ESLint**: Includes accessibility checks, import sorting, and kebab-case file naming
- **Prettier**: Code formatting with Tailwind class sorting

### Git Hooks

- **Husky + lint-staged**: Lints code before commits
- **commitlint**: Enforces Conventional Commits

## Quick Start

```bash
git clone <your-repo-url> my-project
cd my-project
bun install
bun run dev
```

## Scripts

```bash
bun run dev            # Start development server
bun run build          # Build for production
bun run lint           # Run ESLint
bun test               # Run tests
bun run test:ui        # Run tests with UI
bun run test:coverage  # Run tests with coverage
```

## Deployment

### GitHub Pages

1. **Update the base path** in `.github/workflows/deploy.yml`:

```yaml
- name: Build
  run: bun run build
  env:
    VITE_BASE_PATH: /your-repo-name/
```

2. **Enable GitHub Pages** in your repository:
   - Go to Settings → Pages
   - Source: GitHub Actions

3. **Push to main branch** - deployment happens automatically

4. **Your site will be live at:** `https://your-username.github.io/your-repo-name/`

### Vercel / Netlify

No configuration needed! Just connect your repository and deploy.

### Local Preview

```bash
bun run build
bun run preview
```

## Project Conventions

### Absolute Imports

Use `@/*` to import from `src`. Avoid `../` paths.

- **Good:** `import { Button } from '@/components/ui/button'`
- **Bad:** `import { Button } from '../../components/ui/button'`

### File Naming

All files and folders in `src` must be **kebab-case** (e.g., `theme-toggle.tsx`). ESLint enforces this.

- **File:** `theme-toggle.tsx`
- **Component:** `export function ThemeToggle() {...}`

### Testing

Test files use the `.test.tsx` or `.test.ts` extension and follow the same kebab-case convention.

- **Test file:** `theme-toggle.test.tsx`
- **Location:** Co-located with the component or in `__tests__` folders

### Commit Convention

Uses [Conventional Commits](https://www.conventionalcommits.org/). First line must be lowercase.

Examples:

- `feat: add new button component`
- `fix: resolve styling issue on mobile`
- `chore: update dependencies`
- `test: add tests for theme toggle`

## Credits

Architecture inspired by [Bulletproof React](https://github.com/alan2207/bulletproof-react).
