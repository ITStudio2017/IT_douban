$(".book_comment_pinfen_star").hover(function(){
	var total=$(this).index();
	for(var i=0;i<=total;i++)
	{
		$(".book_comment_pinfen_star").eq(i).find("img").attr('src','../images/star.png');
console.log(i);
	}
	for(var j=4;j>total;j--)	
	{
		$(".book_comment_pinfen_star").eq(j).find("img").attr('src','../images/stra.png');
// console.log(i);
	}
})
//点击后的页面定位
$(".body_book_comment").click(function(){
	// window.location.hash = "#abc";
	 console.log("555");
	 location.href = "#firstAnchor";      
});


var now_page=0;
var total_page=2;
//下一页

$(".next_page").click(function(){
	if(now_page<total_page){

	now_page+=1;

	$(".body_comment_content ul").eq(now_page).css({'display':'block'});
	$(".body_comment_content ul").eq(now_page).siblings().css({'display':'none'});
	}
	else{
		$(".last_page_tip").fadeIn();
		$(".last_page_tip").delay(1000).fadeOut(0);
	}

});

//上一页

$(".last_page").click(function(){
	if(now_page>0){	
		now_page-=1;
		$(".body_comment_content ul").eq(now_page).css({'display':'block'});
		$(".body_comment_content ul").eq(now_page).siblings().css({'display':'none'});
	}
	else{
		$(".first_page_tip").fadeIn();
		// $(".last_page").css({'disabled':'true'});
		$(".first_page_tip").delay(1000).fadeOut(0);
	}

	});
	
//首页
$(".first_page").click(function(){
now_page=0;
$(".body_comment_content ul").eq(now_page).css({'display':'block'});
$(".body_comment_content ul").eq(now_page).siblings().css({'display':'none'});
});


//关于点赞
var click_a=0;
$(".body_comment_good_pic").click(function(){
	click_a=click_a-0+1;
	if((click_a-0)%2!=0){
		$(this).find("img").attr('src','../images/good_red.png');
		var pre=$(".body_comment_good_amount_1").html();
		$(".body_comment_good_amount_1").html(pre-0+1);
	}
	else{
		$(this).find("img").attr('src','../images/good_white.png');
		var pre=$(".body_comment_good_amount_1").html();
		$(".body_comment_good_amount_1").html(pre-0-1);
	}
	
})