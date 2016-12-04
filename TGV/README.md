## Endpoint:
Movie info:
- http://<i></i>tgv.api.lb.appxtream.com/

Ticketing:
- http://<i></i>tgv.vista.appxtream.com/



Params:
- \_dc : Epoch

### Example request: 
```
GET http://tgv.api.lb.appxtream.com/jsonFeed.action?_dc=7878564564&service=tgvMobileService&action=getMovieList3&mimeType=application%2Fjson&p1=&page=1&start=0&limit=25
```
### Actions:
- Movie listings 		: <br>`http://tgv.api.lb.appxtream.com/jsonFeed.action?service=tgvMobileService&action=getMovieList3`
-	Movie Info	   		: <br>`http://tgv.api.lb.appxtream.com/jsonFeed.action?service=tgvMobileService&action=getMovieDetail2&p1=TGV-inf1680`
- Movie Purchase 		: <br>`http://tgv.api.lb.appxtream.com/jsonFeed.action?service=tgvMobileService&action=getPurchaseInfoList3&p1=TGV-inf1680&p2=0&p3=0&p4=0&p5=0`
- Movie Purchase info	: <br>`http://tgv.api.lb.appxtream.com/jsonFeed.action?service=tgvMobileService&action=getPurchaseInfoList3&p1=TGV-inf1680&p2=Standard&p3=IP0&p4=26-03-2015&p5=0`
- Movie with Date 	: <br>`http://tgv.api.lb.appxtream.com/jsonFeed.action?service=tgvMobileService&action=getPurchaseInfoList3&p1={INTERNAL MOVIE ID}&p2=Standard&p3={CINEMA ID}&p4=0&p5=0`

###	Artwork Base URL:
- http://<i></i>tgv.static.appxtream.com/

### Extras:
- Web Endpoints:
  - `http://tgv.com.my/dotCMS/salesData?action=getMovies`
  - `https://www.tgv.com.my/Browsing/Movies/Details/h-{Movie ID}`
  
- Example Request:
  - `http://tgv.com.my/dotCMS/salesData?movieId=HO00004073&action=getCinemasByMovie`
