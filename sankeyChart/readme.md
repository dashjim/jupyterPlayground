
**How to setup**

This Sankey chart is based on the one from [github](https://github.com/ricklupton/floweaver) 
and it only supports display in Jupyter notebook for now.
To fix it, here we use a [work around](https://github.com/ricklupton/floweaver/issues/34) to let it
generate picture. The first step is to generate a json file for the chart, then we convert this json
 file to  a svg chart.
 
 Now we have the svg chart to display in a browser and it should be able to reflect the data change,
 we can do it by start any [http server](https://www.npmjs.com/package/http-server) in the folder containing the svg chart, then we can access it
 from browser.
 
 We will also use a chrome plugin to auto refresh the page. Search _auto refresh_ from Chrome app 
 store.
 
 Finally we need the _scheduler.sh_ to generate the json file and svg picture every 4 seconds. You
 can run it with _sh scheduler.sh_ 