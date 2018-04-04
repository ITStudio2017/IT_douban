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




//关于点赞
// var click_a=0;
// $(".body_comment_good_pic").click(function(){
// 	var index = $(".body_comment_good_pic").index(this);

// 	click_a=click_a-0+1;
// 	if((click_a-0)%2!=0){
// 		$(this).find("img").attr('src','../images/good_red.png');
// 		var pre=$(".body_comment_good_amount_1").html();
// 		$(".body_comment_good_amount_1").html(pre-0+1);
// 	}
// 	else{
// 		$(this).find("img").attr('src','../images/good_white.png');
// 		var pre=$(".body_comment_good_amount_1").html();
// 		$(".body_comment_good_amount_1").html(pre-0-1);
// 	}
	
// })
$(".body_comment_good_pic").click(function(){
	var index = $(".body_comment_good_pic").index(this);

	console.log(index);
		var num = parseInt($(".body_comment_good_amount").html()); 
	if($(this).find("img").attr('src') == ('../images/goog.png')){
		$(this).find("img").attr('src','../images/good_red.png');
		var pre=$(".body_comment_good_amount").eq(index).html();
		$(".body_comment_good_amount").eq(index).html(pre-0+1);
	}
	else{
		$(this).find("img").attr('src','../images/goog.png');
		var pre=$(".body_comment_good_amount").eq(index).html();
		$(".body_comment_good_amount").eq(index).html(pre-0-1);
	}
})


//收藏该书
$(".body_book_grade_love").click(function(){
	if($(this).find("img").attr('src') == ("../images/love.png")){
		$(this).find("img").attr('src','../images/grade_love.png')
	}
	
	else{
		$(this).find("img").attr('src','../images/love.png')
	}

});


var time_set=true;
var now_page=0;
var total_page=2;


//下一页

var time_set=true;
$(".next_page").click(function(){
	if(now_page<total_page){
	now_page+=1;
	$(".body_commit_content_list").eq(now_page).css('display','block');
	$(".body_commit_content_list").eq(now_page).siblings().css('display','none');


}
else{
		
		if(time_set==true)
		{

			time_set=false;
			$(".last_page_tip").fadeIn();

			var time_1=setInterval(function(){
				console.log(time_set);
				
			},2000)	
	
			$(".last_page_tip").delay(1000).fadeOut(function(){
				clearInterval(time_1);
				time_set=true;
			
			});
		
		}	
	
		}

});

//上一页

$(".last_page").click(function(){
	if(now_page>0){	
		now_page-=1;
		$(".body_commit_content_list").eq(now_page).css('display','block');
		$(".body_commit_content_list").eq(now_page).siblings().css('display','none');
	}
	else{
		
		if(time_set==true)
		{

			time_set=false;
			$(".first_page_tip").fadeIn();

			var time_1=setInterval(function(){
				console.log(time_set);
				
			},2000)	
	
			$(".first_page_tip").delay(1000).fadeOut(function(){
				clearInterval(time_1);
				time_set=true;
			
			});
		
		}	
	
		}

	});

//首页
$(".first_page").click(function(){
if(now_page == 0){
		if(time_set==true)
		{

			time_set=false;
			$(".first_page_tip").fadeIn(function(){
			var time_1=setInterval(1500)	
			});
			$(".first_page_tip").delay(1000).fadeOut(function(){
			time_set=true;
			// console.log(time_set);
			});
		
		}	

}
now_page=0;
$(".body_commit_content_list").eq(now_page).css({'display':'block'});
$(".body_commit_content_list").eq(now_page).siblings().css({'display':'none'});


});

// $(".next_page").click(function(){
// 	if(now_page<total_page){

// 	now_page+=1;
// console.log($(".body_comment_content_list").eq(0).css('display'));
// 	$(".body_comment_content_list").eq(0).css({'display':'none'});

// 	// $(".body_comment_content_list").eq(now_page).siblings().css({'display':'none'});
// 	}
// 	else{
		
// 		if(time_set==true)
// 		{

// 			time_set=false;
// 			$(".last_page_tip").fadeIn();

// 			var time_1=setInterval(function(){
// 				console.log(time_set);
				
// 			},2000)	
	
// 			$(".last_page_tip").delay(1000).fadeOut(function(){
// 				clearInterval(time_1);
// 				time_set=true;
			
// 			});
		
// 		}	
	
// 		}

// });
// $(".search_box_input").focus(function(){
//   $(this).attr("value","");
//   $(this).css({'color':'black'});
// });
// $(".search_box_input").blur(function(){
// 	var content = $(this).val();
// 	if(content == ""){
		
// 		 $(this).attr("value","请输入图书名称/作者");
// 		// $(this).attr("value",);
// 		$(this).css({'color':'#C9C9C9'});
// 	}

// });