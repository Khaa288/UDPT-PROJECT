<?php
class Calendar extends DateTime
{
    protected $year;
    protected $month_number;
    protected $week_days = [
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ];
    protected $weeks = [];

    public function getYear() {
        return $this->year;
    }

    public function setYear($year) {
        $this->year = $year;
    }

    public function getMonthNumber() {
        return $this->month_number;
    }

    public function setMonthNumber($month_number) {
        $this->month_number = $month_number;
    }

    public function getWeeks() {
        return $this->weeks;
    }

    public function getWeekDays() {
        return $this->week_days;
    }

    public function create() {
        $date = $this->setDate($this->getYear(), $this->getMonthNumber(), 1);

        $daysInMonth = $date->format('t');

        $dayMonthStarts = $date->format('N');

        $days = array_fill(0, $dayMonthStarts - 1, '');
    
        for($x = 1; $x <= $daysInMonth; $x++){
            $days[] = $x;
        }

        $this->weeks = array_chunk($days, 7);
    }
}
?>