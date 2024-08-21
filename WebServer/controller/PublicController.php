<?php 
class PublicController
{
    public function login(){
        // echo $_REQUEST["username"];
        // echo $_REQUEST["password"];

        $VIEW = "./view/ManagerDashboard.phtml";
        require("./template/Layout.phtml");
    }

    public function toHome()
    {
        $VIEW = "./view/ManagerDashboard.phtml";
        require("./template/Layout.phtml");
    }

    public function toLogin() {
        $VIEW = "./view/LoginPage.phtml";
        require($VIEW);
    }

    public function toProfile() {
        $VIEW = "./view/ProfileManagement/ListProfiles.phtml";
        require("./template/Layout.phtml");
    }

    public function toTimesheet() {
        $VIEW = "./view/TimesheetManagement/ListTimesheets.phtml";
        require("./template/Layout.phtml");
    }

    public function toLeave() {
        $VIEW = "./view/LeaveManagement/ListLeaveRequests.phtml";
        require("./template/Layout.phtml");
    }

    public function toWFH() {
        $VIEW = "./view/WFHManagement/ListWFHRequests.phtml";
        require("./template/Layout.phtml");
    }
}
?>