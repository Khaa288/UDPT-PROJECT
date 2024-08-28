<?php 
class WfhController
{
    public function acceptWfh()
    {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($accept_wfh_api.$requestId.'/accept', null, null);

        header("Location: index.php?action=wfh-management&page=1&pageSize=5");
    }

    public function denyWfh()
    {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($deny_wfh_api.$requestId.'/deny', null, null);

        header("Location: index.php?action=wfh-request-management&page=1&pageSize=5");
    }

    public function requestWfh()
    {
        // $VIEW = "./view/TimesheetManagement/TimesheetDetail.phtml";
        // require("./template/Layout.phtml");
    }
}
?>