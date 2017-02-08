/**
 * Created by work on 2/4/2017.
 */
var cl = 0;
$(function () {
    $(document).on('click', 'img', function () {
        cl = 1;
        var tmp2 = $(this).parent().attr("id");
        var tmp = "f" + tmp2.charAt(2) + tmp2.charAt(3);
        $.post("/server", {javad: tmp}, function (data, status) {
            if (status == "success") {
                if (data != 0) {
                    $("table").html(data);
                }
                else {
                    alert("No Permission");
                }
            }
            else {
                alert("There is a problem in Connecting")
            }
        });
    });
    $(document).on('click', 'td', function (event) {
        if (cl) {
            var can = $(this).attr("style");
            if (can == "border: 3px lawngreen solid") {
                var tmp2 = $(this).attr("id");
                var tmp = "m" + tmp2.charAt(2) + tmp2.charAt(3)
                $.post("/server", {javad: tmp}, function (data, status) {
                    if (status == "success") {
                        if (data != 0) {
                            $("table").html(data);
                        }
                        else {
                            alert("No Permission");
                        }
                    }
                    else {
                        alert("There is a problem in Connecting")
                    }
                });
            }
            if (can == "border: 3px green solid") {
                var tmp2 = $(this).attr("id");
                var tmp = "a" + tmp2.charAt(2) + tmp2.charAt(3);
                $.post("/server", {javad: tmp}, function (data, status) {
                    if (status == "success") {
                        if (data != 0) {
                            $("table").html(data);
                        }
                        else {
                            alert("No Permission");
                        }
                    }
                    else {
                        alert("There is a problem in Connecting")
                    }
                });
            }

            if (can != "border: 3px green solid" && can != "border: 3px lawngreen solid") {
                alert(3);
            }
        }
        $(this).off('onclick');
    });
});
