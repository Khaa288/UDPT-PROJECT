<?php
session_start();
require_once("./controller/PublicController.php");
require_once("./controller/ProfileController.php");
require_once("./controller/TimesheetController.php");
require_once("./controller/LeaveController.php");
require_once("./controller/WfhController.php");
require_once("./controller/AttendanceController.php");
require_once("./controller/RewardController.php");
require_once("./api/ApiRequest.php");

$action = "";
if (isset($_REQUEST["action"])) {
    $action = $_REQUEST["action"];
}

switch ($action) {
    case "login":
        $controller = new PublicController();
        $controller->login();
        break;
    case "logout":
        unset($_SESSION["AuthUser"]);  
        $controller = new PublicController();
        $controller->toLogin();
        break;
    case "home":
        $controller = new PublicController();
        $controller->toHome();
        break;
    
    case "attendance":
        $controller = new PublicController();
        $controller->toAttendance();
        break; 
    case "check-in":
        $controller = new AttendanceController();
        $controller->checkIn();
        break; 
    case "check-out":
        $controller = new AttendanceController();
        $controller->checkOut();
        break;   
    
    case "profile-management":
        $controller = new PublicController();
        $controller->toProfileManagement();
        break;
    case "profile":
        $controller = new PublicController();
        $controller->toProfile();
        break; 
    case "update-profile":
        $controller = new ProfileController();
        $controller->updateProfile();
        break; 
    case "deactivate-profile":
        $controller = new ProfileController();
        $controller->deactivateProfile();
        break;  
    
    case "employee-leave-request-management":
        $controller = new PublicController();
        $controller->toEmployeeLeaveRequest();
        break;
    case "employee-apply-leave":
        $controller = new PublicController();
        $controller->toApplyLeave();
        break;
    case "leave-apply":
        $controller = new LeaveController();
        $controller->applyLeave();
        break;
    case "leave-request-management":
        $controller = new PublicController();
        $controller->toLeaveRequest();
        break;
    case "leave-management":
        $controller = new PublicController();
        $controller->toLeave();
        break;
    case "accept-leave":
        $controller = new LeaveController();
        $controller->acceptLeave();
        break;
    case "deny-leave":
        $controller = new LeaveController();
        $controller->denyLeave();
        break;

    case "employee-wfh-request-management":
        $controller = new PublicController();
        $controller->toEmployeeWFHRequest();
        break;
    case "employee-apply-wfh":
        $controller = new PublicController();
        $controller->toApplyWFH();
        break;
    case "wfh-apply":
        $controller = new WfhController();
        $controller->applyWfh();
        break;
    case "wfh-management":
        $controller = new PublicController();
        $controller->toWFH();
        break;  
    case "wfh-request-management":
        $controller = new PublicController();
        $controller->toWFHRequest();
        break;
    case "accept-wfh":
        $controller = new WfhController();
        $controller->acceptWfh();
        break;
    case "deny-wfh":
        $controller = new WfhController();
        $controller->denyWfh();
        break;
    
    case "timesheet-management":
        $controller = new PublicController();
        $controller->toTimesheet();
        break;
    case "timesheet-request-management":
        $controller = new PublicController();
        $controller->toTimesheetRequest();
        break;   
    case "timesheet-detail":
        $controller = new TimesheetController();
        $controller->toTimesheetDetail();
        break;
    case "update-timesheet":
        $controller = new TimesheetController();
        $controller->updateTimesheet();
        break;
    case "request-update-timesheet":
        $controller = new TimesheetController();
        $controller->requestUpdateTimesheet();
            break;
    case "accept-timesheet-update":
        $controller = new TimesheetController();
        $controller->acceptUpdateRequest();
        break;
    case "deny-timesheet-update":
        $controller = new TimesheetController();
        $controller->denyUpdateRequest();
        break;

    case "reward-management":
        $controller = new PublicController();
        $controller->toVouchers();
        break;
    case "my-reward-management":
        $controller = new PublicController();
        $controller->toMyVouchers();
        break;
    case "collect-voucher":
        $controller = new RewardController();
        $controller->collectVoucher();
        break;
    case "to-send-point":
        $controller = new PublicController();
        $controller->toSendPoint();
        break;
    case "send-point":
        $controller = new RewardController();
        $controller->sendPoint();
        break;

    default:
        $controller = new PublicController();
        $controller->toLogin();
}
