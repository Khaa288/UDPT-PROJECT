<?php 
class LeaveController
{
    public function acceptLeave()
    {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($accept_leave_api.$requestId.'/accept', null, null);

        header("Location: index.php?action=leave-management&page=1&pageSize=5");
    }

    public function denyLeave()
    {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($deny_leave_api.$requestId.'/deny', null, null);

        header("Location: index.php?action=leave-request-management&page=1&pageSize=5");
    }

    public function requestLeave()
    {
        // $VIEW = "./view/TimesheetManagement/TimesheetDetail.phtml";
        // require("./template/Layout.phtml");
    }
}
?>