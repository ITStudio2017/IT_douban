var time_set=true;
var now_page=0;
var total_page=2;
//下一页
var time_set=true;
$(".next_page").click(function(){
	if(now_page<total_page){

	now_page+=1;

	$(".body_comment_contentout ul").eq(now_page).css({'display':'block'});
	$(".body_comment_contentout ul").eq(now_page).siblings().css({'display':'none'});
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
		$(".body_comment_contentout ul").eq(now_page).css({'display':'block'});
		$(".body_comment_contentout ul").eq(now_page).siblings().css({'display':'none'});
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
$(".body_comment_contentout ul").eq(now_page).css({'display':'block'});
$(".body_comment_contentout ul").eq(now_page).siblings().css({'display':'none'});


});

//关于点赞

	
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
	
	



// })
// if(praise_img.attr("src") == ("Images/yizan.png")

//搜索框
$(".search_box_input").focus(function(){
  $(this).attr("value","");
  $(this).css({'color':'black'});
});
$(".search_box_input").blur(function(){
	var content = $(this).val();
	if(content == ""){
		
		 $(this).attr("value","请输入图书名称/作者");
		// $(this).attr("value",);
		$(this).css({'color':'#C9C9C9'});
	}

});

//时间热度标签的切换
// $(".book_comment_nav_hot").click(function(){
// 	$(this).css({'background-color':'#02c39a'});
// 	$(".body_comment_contentout").css('display','none');
// 	$(".hot").css('display','block');
// })

// $(".book_comment_nav_time").click(function(){
// 	$(this).css({'background-color':'#02c39a'});

// 	$(".body_comment_contentout").css('display','none');
// 	$(".time").css('display','block');
// })

//收藏
$(".body_article_author_love").click(function(){
	$(this).find("img").attr('src','../images/love_red2.png')
})