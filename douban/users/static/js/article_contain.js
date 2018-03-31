
var now_page=0;
var total_page=2;
//下一页
var time_set=true;
$(".next_page").click(function(){
	if(now_page<total_page){

	now_page+=1;

	$(".body_comment_content ul").eq(now_page).css({'display':'block'});
	$(".body_comment_content ul").eq(now_page).siblings().css({'display':'none'});
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
		$(".body_comment_content ul").eq(now_page).css({'display':'block'});
		$(".body_comment_content ul").eq(now_page).siblings().css({'display':'none'});
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
	if(now_page=0)
	{
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

