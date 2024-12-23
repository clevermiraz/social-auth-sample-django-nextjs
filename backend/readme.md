---

## 🛠️ Editor Setup (Optional)

### Recommended Editor: **VS Code**

### Install Extensions:

-   **Flake8**
-   **Autopep8**

### Configure VS Code:

Create or update `.vscode/settings.json` with the following configuration:

```json
{
    "editor.fontFamily": "Fira Code, Operator Mono",
    "editor.fontWeight": "400",
    "editor.fontLigatures": true,
    "editor.wordWrap": "on",
    "editor.minimap.enabled": false,
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": ["comment", "comment.block.documentation", "string.quoted"],
                "settings": {
                    "fontStyle": "italic"
                }
            }
        ]
    },
    "editor.cursorSmoothCaretAnimation": "on",
    "editor.cursorBlinking": "expand",
    "editor.fontSize": 15,
    "editor.lineHeight": 26,
    "editor.formatOnSave": true,
    "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    },
    "[django-html]": {
        "editor.quickSuggestions": {
            "other": true,
            "comments": true,
            "strings": true
        },
        "editor.formatOnSave": false
    },
    "terminal.integrated.fontSize": 14,
    "terminal.integrated.fontFamily": "Victor Mono, Operator Mono",
    "workbench.colorTheme": "Learn with Sumit Theme",
    "prettier.printWidth": 120,
    "emmet.includeLanguages": {
        "django-html": "html"
    }
}
```

### Linting Setup:

Create a `.flake8` file in the project root directory with the following content:

```ini
[flake8]
exclude = .git,__pycache__,docs/source/conf.py,old,build,dist
max-line-length = 160
max-complexity = 50
select = C,E,F,W,B,B950
ignore = E203, E501, W503
```

---

## 🔄 Pipenv Usage

### Export Dependencies to `requirements.txt`

```bash
pipenv requirements > requirements.txt
```
