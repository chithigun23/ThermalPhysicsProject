package com.example.ex1;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void showHelloWorld(View view) {
        Toast.makeText(this, "Hello World!", Toast.LENGTH_SHORT).show();
    }
}

