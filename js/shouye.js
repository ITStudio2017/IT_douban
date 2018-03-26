//手风琴
// $(".body_top_sfq_pic_1").click(function(){
// 	$(this).stop(true).animate({width:"572px"},60).siblings().stop(true).animate({width:"106px"},60);
// });
// $(".body_top_sfq_pic_2").click(function(){
// 	$(this).stop(true).animate({width:"572px"},60).siblings().stop(true).animate({width:"106px"},60);
// });
// $(".body_top_sfq_pic_3").click(function(){
// 	$(this).stop(true).animate({width:"572px"},60).siblings().stop(true).animate({width:"106px"},60);
// });
// $(".body_top_sfq_pic_4").click(function(){
// 	$(this).stop(true).animate({width:"572px"},60).siblings().stop(true).animate({width:"106px"},60);
// });
// $(".body_top_sfq_pic_5").click(function(){
// 	$(this).stop(true).animate({width:"572px"},60).siblings().stop(true).animate({width:"106px"},60);
// });

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