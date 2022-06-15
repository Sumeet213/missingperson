class GFG
{
// function to find angle between
// hour hand and minute hand
static float calcAngle(int hh, int mm)
{
    // Calculate the angles moved by hour and
    // minute hands with reference to 12:00
    float hour_angle = 0.5f * (hh * 60 + mm);
    float minute_angle = 6 * mm;
 
    // Find the difference between two angles
    float angle = Math.abs(hour_angle - minute_angle);
 
    // Return the smaller angle of
    // two possible angles
    angle = Math.min(360-angle, angle);
 
    return angle;
}
 
// function to print all time when
// angle between hour hand and minute
// hand is theta
static void printTime(float theta)
{
    for (int hh = 0; hh < 12; hh++)
    {
        for (int mm = 0; mm < 60; mm++)
        {
            if (calcAngle(hh, mm) == theta)
            {
                System.out.println(hh + ":" + mm);
                return;
            }
        }
    }
     
    System.out.println("Input angle not valid.");
    return;
}
 
// Driver code
public static void main (String[] args)
{
    float theta = 90.0f;
    printTime(theta);
}
}
 