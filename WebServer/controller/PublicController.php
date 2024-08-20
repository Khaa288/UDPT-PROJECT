<?php 
class PublicController
{
    public function index()
    {
        $VIEW = "./view/Dashboard.phtml";
        $VIEW = "./view/ProfileManagement/ListProfiles.phtml";
        $VIEW = "./view/LeaveManagement/ListLeaveRequests.phtml";
        $VIEW = "./view/WFHManagement/ListWFHRequests.phtml";
        
        require("./template/Layout.phtml");
    }
}
?>