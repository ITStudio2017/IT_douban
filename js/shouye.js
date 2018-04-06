//手风琴


// $(".body_top_inner ul li").click(function(){
// 	$(".body_top_inner ul li").stop(true);
// 	$(this).animate({'width':"572px"},800).siblings().animate({'width':"106px"},800);
// });
//搜索框
// $(".search_box_input").click(function(){
// 	$(this).attr("value","");
// });
// $(".search_box_input").blur(function(){
// 	$(this).attr("value","请输入关键词");
// });



// var mar_left = $(".body_top_inner ul li").each(function(index){
// $(this).width();

// })
var mar_left = new Array();
 mar_left[0] = $(".body_top_sfq_pic_1 ").width()/2;
 mar_left[1] = $(".body_top_sfq_pic_2").width();
 mar_left[2] = $(".body_top_sfq_pic_3").width();
 mar_left[3] = $(".body_top_sfq_pic_4").width();
 mar_left[4] = $(".body_top_sfq_pic_5").width();

// $(".body_top_inner ul img").eq(0).css('margin-left',-mar_left[0]);


// (parseInt(this.parentNode.style.width) - this.width) /2 + 'px



//加入收藏

$(".body_hotbook_book_love_1").click(function(){
	if($(this).find("img").attr('src') == ("../images/love.png")){
		$(this).find("img").attr('src','../images/love_red2.png')
	}
	
	else{
		$(this).find("img").attr('src','../images/love.png')
	}

});





var json0 = { "width":106, "height":327, "top":0, "left":0 ,"z-index":10 ,"opacity":0.6 };

var json1 = { "width":106, "height":327, "top":0, "left":106 ,"z-index":20 ,"opacity":0.6}

var json2 = { "width":572, "height":327, "top":0, "left":212 ,"z-index":50 ,"opacity":1}

var json3 = { "width":106, "height":327, "top":0, "left":784 ,"z-index":20 ,"opacity":0.6}

var json4 = { "width":106, "height":327, "top":0, "left":890 ,"z-index":10 ,"opacity":0.6}

// var json5 = { "width":80, "height":54, "top":71, "left":556}

// var json6 = { "width":48, "height":32, "top":93, "left":693 }


$(".red").click(function(){

	
	
	

	// if(click_num) (num)
	if(!$(".body_top_inner_sfq li").is(":animated")){
	$(".body_top_sfq_pic_2").animate(json0,800);
	$(".body_top_sfq_pic_3").animate(json1,800);
	$(".body_top_sfq_pic_4").animate(json2,800);
	$(".body_top_sfq_pic_5").animate(json3,800);
	$(".body_top_sfq_pic_1").animate(json4,800);
	// $(".body_top_sfq_pic_1").animate(json0,400);
	// $(".body_top_sfq_pic_1").attr("class","body_top_sfq_pic_5")
	$(".body_top_sfq_pic_2").attr("class","body_top_sfq_pic_1")
	$(".body_top_sfq_pic_3").attr("class","body_top_sfq_pic_2")
	$(".body_top_sfq_pic_4").attr("class","body_top_sfq_pic_3")
	$(".body_top_sfq_pic_5").attr("class","body_top_sfq_pic_4")
	if($(".body_top_sfq_pic_4").next().length != 0)
	{
		$(".body_top_sfq_pic_4").next().attr("class","body_top_sfq_pic_5")
	}
	else{
		
		$(".body_top_inner_sfq li:first").attr("class","body_top_sfq_pic_5");
		
	}

	var sfq_title;
	if($(".body_top_sfq_word").each(function(index){
		$(this).eq(index).parent('.sfq_pic').width() == "572";
		sfq_title = index;
	})
		){

		$(".body_top_sfq_word").eq(sfq_title - 0).css('display', 'block');
		console.log(sfq_title)
	}
	else{
		$(".body_top_sfq_word").eq(sfq_title - 0).siblings().css('display', 'none');
	}
}
	

	// $(".body_top_inner_sfq li:first").attr("class","body_top_sfq_pic_5")
	// $(".body_top_sfq_pic_2").attr("class","body_top_sfq_pic_1")
})
// $("")
//向右翻页
$(".blue").click(function(){

	
	
	

	// if(click_num) (num)
	if(!$(".body_top_inner_sfq li").is(":animated")){
	$(".body_top_sfq_pic_1").animate(json1,800);
	$(".body_top_sfq_pic_2").animate(json2,800);
	$(".body_top_sfq_pic_3").animate(json3,800);
	$(".body_top_sfq_pic_4").animate(json4,800);
	$(".body_top_sfq_pic_5").animate(json0,800);
	// $(".body_top_sfq_pic_1").animate(json0,400);
	// $(".body_top_sfq_pic_1").attr("class","body_top_sfq_pic_5")
	$(".body_top_sfq_pic_4").attr("class","body_top_sfq_pic_5")
	$(".body_top_sfq_pic_3").attr("class","body_top_sfq_pic_4")
	$(".body_top_sfq_pic_2").attr("class","body_top_sfq_pic_3")
	$(".body_top_sfq_pic_1").attr("class","body_top_sfq_pic_2")
	if($(".body_top_sfq_pic_2").prev().length != 0)
	{
		$(".body_top_sfq_pic_2").prev().attr("class","body_top_sfq_pic_1")
	}
	else{
		
		$(".body_top_inner_sfq li:last").attr("class","body_top_sfq_pic_1");
		
	}
	
	}

	// $(".body_top_inner_sfq li:first").attr("class","body_top_sfq_pic_5")
	// $(".body_top_sfq_pic_2").attr("class","body_top_sfq_pic_1")
})

