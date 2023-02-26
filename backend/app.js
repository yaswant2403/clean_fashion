const express = require('express')
const app = express()
const port = 3000

//import data from './mock_data.json' assert { type: 'json' }
const config = require('./mock_data.json')
console.log(config)

for (id in config) {
app.get('/', (req, res) => {
  // for (let x in config) {
  //   res.send(x)
  // }
  res.send('Hello World!')
})
}

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
