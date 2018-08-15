
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
 
 
 **For mysql integration**
 
 ```
 create table flow(
 id int(20) primary key not null auto_increment,
 app_operation_end  varchar(50),
 menu varchar(50),  
 target varchar(20),
 value int(200)
 );
 ```
 
 Mapping from menu to Chinese meaning
```
0001     -->      欢迎词     
1010     -->      延迟还款业务
1020     -->      账单分期业务
1030     -->      分期优惠活动
1040     -->      其它
1210     -->      查询密码重置
1220     -->      交易密码重置
1230     -->      修改交易密码
1240     -->      其它
```

**Team Viewer**


382 345 370
g e m     831


 
 
 
 
 