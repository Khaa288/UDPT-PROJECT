<?php 
class AttendanceController
{
    public function checkIn()
    {
        require("./api/Endpoints.php");

        $body = array (
            'Employee' => json_decode($_REQUEST["employee"]),
            'CheckInNote' => $_REQUEST["checkInNote"]
        );

        $response = ApiRequest::post($check_in_api, null, $body);

        header("Location: index.php?action=attendance");
    }

    public function checkOut()
    {
        require("./api/Endpoints.php");
        
        $body = array (
            'Employee' => json_decode($_REQUEST["employee"]),
            'CheckOutNote' => $_REQUEST["checkOutNote"]
        );

        $response = ApiRequest::post($check_out_api, null, $body);

        header("Location: index.php?action=attendance");
    }
}
?>