const print = require('print')

print.out(`
This is a file that will be commited to git based on the established .gitignore
file while the node_modules folder will not. That's why you can't see it, but
recalling npm install in the directory while recreate the node_modules folder
using the dependencies listed in the package.json file.
`)