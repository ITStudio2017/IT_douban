//出现删除和详情
$(".personal_body_save_book_1").mouseenter(function(){
	var num=$(this).index();
	$(".personal_body_save_book_more_1").eq(num).fadeIn();
	// $(".personal_body_save_book_more_1").eq(num).siblings().();
})
$(".personal_body_save_book_1").mouseleave(function(){
	var num=$(this).index();
	$(".personal_body_save_book_more_1").eq(num).fadeOut();


})
// $(".personal_body_save_book_2").mouseenter(function(){
// 	var num=$(this).index();
// 	$(".personal_body_save_book_more_1").eq(num).fadeIn();
// })
// $(".personal_body_save_book_2").mouseleave(function(){
// 	var num=$(this).index();
// 	$(".personal_body_save_book_more_1").eq(num).fadeOut();


// })
// $(".personal_body_save_book_3").mouseenter(function(){
// 	var num=$(this).index();
// 	$(".personal_body_save_book_more_1").eq(num).fadeIn();
// })
// $(".personal_body_save_book_3").mouseleave(function(){
// 	var num=$(this).index();
// 	$(".personal_body_save_book_more_1").eq(num).fadeOut();


// })
// $(".personal_body_save_book_4").mouseenter(function(){
// 	var num=$(this).index();
// 	$(".personal_body_save_book_more_1").eq(num).fadeIn();

// })
// $(".personal_body_save_book_4").mouseleave(function(){
// 	var num=$(this).index();
// 	$(".personal_body_save_book_more_1").eq(num).fadeOut();

// })




//删除图书
$(".personal_body_save_book_del_1").click(function(){
	var num=$(this).index();
	$(".personal_body_save_book_inner ul li").eq(num).remove();
});



