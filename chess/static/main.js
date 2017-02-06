/**
 * Created by work on 2/4/2017.
 */
$(function(){
   $("img").click(function(){
      var tmp=$(this).parent().html();
      var tmp2=$(this).parent().attr("id");
      $("td").click(function(){
         /*$.post("/ali",{javad: 'h'}, function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
         });*/
         var td="#"+tmp2;
         $(td).empty();
         $(this).html(tmp);

      });
   });
});
