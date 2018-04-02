//手风琴


$(".body_top_inner ul li").click(function(){
	$(".body_top_inner ul li").stop(true);
	$(this).animate({'width':"572px"},800).siblings().animate({'width':"106px"},800);
});
//搜索框
$(".search_box_input").click(function(){
	$(this).attr("value","");
});
$(".search_box_input").blur(function(){
	$(this).attr("value","请输入关键词");
});



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