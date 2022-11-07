<?php
    $fav=$_POST["fav"];
    $name=$_POST["name"];
    $con=mysqli_connect("goorm-rds.czbek9smdd2l.ap-northeast-2.rds.amazonaws.com","admin","adminadmin","dbtest") or die("Can't access DB");
    $fav_data=implode(",",$fav);
    $query= "insert into vote (name,favorite) values ('".$name."','".$fav_data."')";
    $result=mysqli_query($con,$query);
    if ($result){
        ?>
        <script> alert("투표가 완료되었습니다"); location.href="..";</script>
        <?php
    }
    else{
        ?>
        <script> alert("투표가 완료되지 않았습니다. \n 다시 시도해 주세요"); location.href=".." </script>
        <?php
    }
    ?>

?>