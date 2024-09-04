<?php 
class ActivityController
{
    public function toActivityDetail()
    {
        require("./api/Endpoints.php");
        $activity_id = $_REQUEST["activityId"];
        $participants = ApiRequest::get($get_participant_activityId.($activity_id),null);
        $activity = ApiRequest::get($get_activities_id_api.($activity_id),null);
        $pages = ApiRequest::get($get_profiles_pages_api, null);
        $employees = ApiRequest::get($get_profiles_api, array(
            'page' => 1,
            'pageSize' => 5
        ));
        $VIEW = "./view/ActivityManagement/ActivityDetail.phtml";
        require("./template/Layout.phtml");
    }
        public function updateActivity()
    {
        require("./api/Endpoints.php");
        $activity_id = $_REQUEST["activityId"];

        $body = array(
            "ActivityName" => $_REQUEST["activityName"],
            "StartTime" => $_REQUEST["startTime"],
            "EndTime" => $_REQUEST["endTime"]
        );

        ApiRequest::put($update_activity_api.$activity_id,null,$body);
        header("Location: index.php?action=activity-management");

    }
    public function createActivity(){
        require("./api/Endpoints.php");
        $body = array(
            "ActivityName" => $_REQUEST["activityName"],
            "StartTime" => $_REQUEST["startTime"],
            "EndTime" => $_REQUEST["endTime"]
        );
        ApiRequest::post($create_activity_api,null,$body);
        header("Location: index.php?action=activity-management");

    }
    public function authorizeStrava(){
        ini_set("allow_url_fopen", 1);
        $code = $_REQUEST["code"];
        $token = ApiRequest::post("https://www.strava.com/oauth/token?client_id=132704&client_secret=2651e938348513bcc96f9e87067d1aec76723831&code=$code&grant_type=authorization_code",null,null);
        print_r($token);
        $otps = array(
            'http' => array(
                'method' => "GET",
                'header' => "Authorization: Bearer $token->access_token"
            )
            );
            $context = stream_context_create($otps);
            $activities = file_get_contents("https://www.strava.com/api/v3/athlete/activities",false,$context);
            
            $activities = json_decode($activities);
            print_r($activities);
    }
    
    

}

?>