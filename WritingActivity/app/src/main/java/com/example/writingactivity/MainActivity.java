package com.example.writingactivity;

import android.app.Dialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.AppCompatButton;
import android.view.View;
import android.view.Window;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
   // AppCompatButton submit;
    EditText editTextThought;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void onSubmit(View view)
    {
        /*submit = (AppCompatButton) findViewById(R.id.SubmitButton);
        editTextThought = (EditText) findViewById(R.id.thought);
        String sThought = editTextThought.toString().trim();
        Toast.makeText(MainActivity.this,sThought,Toast.LENGTH_LONG).show();*/
    }

    public void onFontSelect(View view)
    {

    }
}
