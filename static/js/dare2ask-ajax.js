// Adds an event handler to the element with id #likes - the button
$('.likes').click(function(){
    var upvoteid;
    upvoteid = $(this).attr("data-upvoteid");
    console.log("qid="+upvoteid);
    $.get('/dare2ask/like/', {like_id: upvoteid}, function(data){ //like_id passing to views.py
        // Code to display the updated number of likes for every question in the view.
        console.log(data);
        var likes = data.split(" ");
        $('.like_count').each(function(index) {
          $(this).text(likes[index]);
        });
        //$('#likes').hide();
  });
});
