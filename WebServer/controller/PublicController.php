<?php 
class PublicController
{
    public function index()
    {
        $VIEW = "./view/Dashboard.phtml";
        
        // $VIEW = "./view/LoginPage.phtml";
        // $VIEW = "./view/ProfileManagement/ListProfiles.phtml";
        // $VIEW = "./view/LeaveManagement/ListLeaveRequests.phtml";
        // $VIEW = "./view/WFHManagement/ListWFHRequests.phtml";
        // $VIEW = "./view/TimesheetManagement/ListTimesheets.phtml";
        $VIEW = "./view/TimesheetManagement/TimesheetDetail.phtml";
        
        require("./template/Layout.phtml");
    }
}
?>