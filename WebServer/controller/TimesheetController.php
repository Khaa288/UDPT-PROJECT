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
}
?>