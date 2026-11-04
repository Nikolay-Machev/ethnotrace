// Generate the committed example with the browser's actual report formatter.
const fs = require('node:fs');
const vm = require('node:vm');
const {evidenceReport} = require('../web/report.js');
const context = vm.createContext({window: {}});
vm.runInContext(fs.readFileSync('web/data.js', 'utf8'), context);
const data = context.window.ETHNOTRACE_DATA;
const account = data.claims.find(item => item.id === 'T008');
fs.mkdirSync('docs/reports', {recursive: true});
fs.writeFileSync('docs/reports/T008-evidence.md',
  '<!-- Generated, do not edit. Run python3 scripts/rebuild.py. -->\n\n' +
  evidenceReport(account, data, 'hybrid'));
