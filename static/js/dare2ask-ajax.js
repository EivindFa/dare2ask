// Adds an event handler to the element with id #likes - the button
$('#likes').click(function(){
    var upvoteid;
    upvoteid = $(this).attr("data-upvoteid");
    console.log(upvoteid);
    $.get('/dare2ask/like/', {like_id: upvoteid}, function(data){ //like_id passing to views.py
        $('#like_count').html(data);
        console.log('#like_count');
            $('#likes').hide();
  });
});
