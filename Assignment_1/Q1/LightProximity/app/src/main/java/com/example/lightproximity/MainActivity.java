package com.example.lightproximity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import java.util.EventListener;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    //    Instance of SensorManager and two sensors.
    private SensorManager sensorManager;
    private Sensor proximitySensor;
    private Sensor lightSensor;

    //    Text View for sensor data.
    TextView proximityDataShow;
    TextView lightDataShow;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        proximityDataShow = (TextView) findViewById(R.id.textView6);
        lightDataShow = (TextView) findViewById(R.id.textView4);

//        Instance of the sensor manager from system services.
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
//        Get instances of the light and proximity sensors.
        proximitySensor = sensorManager.getDefaultSensor(Sensor.TYPE_PROXIMITY);
        lightSensor = sensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);

//        If sensor not found in device.
        if (null == proximitySensor) {
            Log.e("proximity-NULL", getResources().getString(R.string.sensor_error));
        }
        if (null == lightSensor) {
            Log.e("light-NULL", getResources().getString(R.string.sensor_error));
        }
    }

    @Override
    protected void onStart() {
        super.onStart();

//        Register sensor listeners on start of the activity.
        if (null != proximitySensor) {
            sensorManager.registerListener(this, proximitySensor,
                    SensorManager.SENSOR_DELAY_NORMAL);
        }
        if (null != lightSensor) {
            sensorManager.registerListener(this, lightSensor,
                    SensorManager.SENSOR_DELAY_NORMAL);
        }
    }

    @Override
    protected void onStop() {
        super.onStop();

//        Unregister sensor listeners on start of the activity.
        sensorManager.unregisterListener(this);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
//        Get the type of sensor and value.
        int sensorType = event.sensor.getType();
        float sensorValue = event.values[0];

//        Update Text View with current sensor data.
        switch (sensorType) {
            case Sensor.TYPE_LIGHT:
                Log.i("light-sensor", "" + sensorValue);
                lightDataShow.setText(sensorValue + " lux");
                break;
            case Sensor.TYPE_PROXIMITY:
                Log.i("prox-sensor", "" + sensorValue);
                proximityDataShow.setText(sensorValue + "");
                break;
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }
}