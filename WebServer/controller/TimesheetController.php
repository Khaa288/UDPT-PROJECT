<?php 
class TimesheetController
{
    public function toTimesheetDetail()
    {
        require("./api/Endpoints.php");

        $timesheet_id = $_REQUEST["timesheetId"];

        $timesheet = ApiRequest::get($get_timesheet_by_id_api.$timesheet_id, null);

        $VIEW = "./view/TimesheetManagement/TimesheetDetail.phtml";
        require("./template/Layout.phtml");
    }

    public function updateTimesheet() {
        require("./api/Endpoints.php");

        $timesheet_id = $_REQUEST["timesheetId"];

        $body = array(
            "Date" =>   $_REQUEST["date"],
            "NewWorkHour" =>  $_REQUEST["newWorkHour"]
        );

        $response = ApiRequest::post($update_timesheet_by_id_api.$timesheet_id, null, $body);

        header("Location: index.php?action=timesheet-detail&timesheetId=".$timesheet_id);
    }

    public function acceptUpdateRequest() {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($accept_update_timesheet_api.$requestId.'/accept', null, null);

        header("Location: index.php?action=timesheet-request-management&page=1&pageSize=5");
    }

    public function denyUpdateRequest() {
        require("./api/Endpoints.php");
        $requestId = $_REQUEST["requestId"];

        $response = ApiRequest::post($deny_update_timesheet_api.$requestId.'/deny', null, null);

        header("Location: index.php?action=timesheet-request-management&page=1&pageSize=5");
    }

    public function requestUpdateTimesheet() {
        
    }
}
?>