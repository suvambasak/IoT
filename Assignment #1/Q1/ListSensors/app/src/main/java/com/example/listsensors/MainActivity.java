leave package com.example.listsensors;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

//    instance of SensorManager
    private SensorManager sensorManager;
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        instance of the sensor manager from system services
        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        List<Sensor> sensorList = sensorManager.getSensorList(Sensor.TYPE_ALL);
//        List to hold all sensor name for adoptor.
        List<String> sensorName = new ArrayList<>();

//        Adding all the sensor name to List of string.
        for(Sensor sensor : sensorList){
            Log.i("sensor",sensor.getName());
            sensorName.add(sensor.getName());
        }

//        Setting the List View with the list of sensor names.
        ArrayAdapter<String> adapter = new ArrayAdapter<String>(MainActivity.this, android.R.layout.simple_dropdown_item_1line,sensorName);
        listView = (ListView) findViewById(R.id.list);
        listView.setAdapter(adapter);
    }
}