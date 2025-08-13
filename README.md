# NB36 ↔ Taktile GitHub Integration

This repository enables automated updates of Taktile Code Nodes via GitHub Actions.

## 🔧 Setup

1. Place your Code Node files inside `code/`
2. Create `config.json` mapping files to node IDs:
   ```json
   {
     ""Summarize.py": {"
   }
Store the following secrets in GitHub:
TAKTILE_API_KEY
TAKTILE_ORG_ID

Merge changes to main — the workflow will deploy automatically 🎉

📞 Need Help?
Contact Taktile Support.
