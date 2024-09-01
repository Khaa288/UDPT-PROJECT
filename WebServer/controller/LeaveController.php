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

        $role = json_decode($_SESSION["AuthUser"])->Role;

        if ($role == 'Employee') {
            header("Location: index.php?action=employee-leave-request-management&page=1&pageSize=5");
        }
        else if ($role == 'Manager') {
            header("Location: index.php?action=leave-request-management&page=1&pageSize=5");
        }

        else {
            header("Location: index.php?action=logout");
        }
    }

    public function applyLeave()
    {
        require("./api/Endpoints.php");

        $employee_id = json_decode($_SESSION["AuthUser"])->EmployeeId;

        $employee = ApiRequest::get($get_profile_by_id_api.$employee_id, null, null);

        $request_employee = array(
            'EmployeeId' => $employee->EmployeeId,
            'EmployeeName' => $employee->FirstName . ' ' . $employee->MiddleName . ' ' . $employee->LastName,
            'EmployeeIdCardNum' => $employee->IdCardNum,
            'EmployeeJobTitle' => $employee->JobTitle
        );

        $from_date = date("d-m-Y", strtotime($_REQUEST["fromDate"]));
        $toDate = date("d-m-Y", strtotime($_REQUEST["toDate"]));
        $note = $_REQUEST["note"];

        $body = array(
            'Employee' => $request_employee,
            'FromDate' => $from_date,
            'ToDate' => $toDate,
            'Note' => $note
        );

        $response = ApiRequest::post($request_leave_api, null, $body);

        header("Location: index.php?action=employee-leave-request-management&page=1&pageSize=5");
    }
}
?>