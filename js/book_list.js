//评分
function star(){
	var grade_1=$(".body_middle_book_grade_num_1").html();
	
	grade_1=(grade_1-0)/2;
	var grade_1_star1=Math.floor(grade_1)

	for(var i=0;i<grade_1_star1;i++)
	{

		$(".body_middle_book_grade_star_1").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_1_star2=grade_1-0-grade_1_star1;
	
	if(grade_1_star2!=0){
		$(".body_middle_book_grade_star_1").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
	
//////////////////////////////////////////////////
	var grade_2=$(".body_middle_book_grade_num_2").html();
	
	grade_2=(grade_2-0)/2;
	
	var grade_2_star1=Math.floor(grade_2)

	for(var i=0;i<grade_2_star1;i++)
	{

		$(".body_middle_book_grade_star_2").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_2_star2=grade_2-0-grade_2_star1;
	
	if(grade_2_star2!=0){
		$(".body_middle_book_grade_star_2").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}

	//////////////////////////////////////////////////
	var grade_3=$(".body_middle_book_grade_num_3").html();
	
	grade_3=(grade_3-0)/2;
	var grade_3_star1=Math.floor(grade_3)
	
	for(var i=0;i<grade_3_star1;i++)
	{

		$(".body_middle_book_grade_star_3").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_3_star2=grade_3-0-grade_3_star1;
	if(grade_3_star2!=0){
		$(".body_middle_book_grade_star_3").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
		//////////////////////////////////////////////////
	var grade_4=$(".body_middle_book_grade_num_4").html();
	
	grade_4=(grade_4-0)/2;
	var grade_4_star1=Math.floor(grade_4)
	
	for(var i=0;i<grade_4_star1;i++)
	{

		$(".body_middle_book_grade_star_4").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_4_star2=grade_4-0-grade_4_star1;
	if(grade_4_star2!=0){
		$(".body_middle_book_grade_star_4").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
		//////////////////////////////////////////////////
	var grade_5=$(".body_middle_book_grade_num_5").html();
	
	grade_5=(grade_5-0)/2;
	var grade_5_star1=Math.floor(grade_5)
	
	for(var i=0;i<grade_5_star1;i++)
	{

		$(".body_middle_book_grade_star_5").append("<li class='body_middle_book_grade_star_inside'><img src='../images/whole_star.png'/></li>");

	}

	var grade_5_star2=grade_5-0-grade_5_star1;
	if(grade_5_star2!=0){
		$(".body_middle_book_grade_star_5").append("<li class='body_middle_book_grade_star_inside'><img src='../images/half_star.png'/></li>");
		
	}
}
star();