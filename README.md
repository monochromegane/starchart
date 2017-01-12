# StarChart

StarChart is a tool to manage [Google Cloud Machine Learning](https://cloud.google.com/products/machine-learning/) training programs and model versions.

## Usage

### Workflow

1. Manage your training programs.

  ```
  .
  ├── MODEL_NAME
  │   ├── setup.py
  │   └── trainer
  │       ├── __init__.py
  │       └── task.py
  └── MODEL_NAME
      └── ...
  ```

2. Train your training programs.

  ```sh
  $ starchart train ...
  ```

  StarChart uploads your training program to cloud storage and submit train job.
  You may not have to worry about job id, and cloud storage training paths.

3. Expose your model.

  ```sh
  $ starchart expose ...
  ```

  StarChart create model and version from your successful jobs.
  And it dumps a model file which define model and version information.

4. Change default version.

   ```sh
   $ starchart apply ...
   ```

   StarChart set default version followed by the model file `isDefault` parameter.

### Commands

```sh
# Train
$ starchart train \
  --project-id=YOUR_PROJECT_ID \
  --package-path=PACKAGE_PATH  \
  --module-name=MODULE_NAME    \
  --region=REGION              \
  --                           \
  --your_train_param=FOO

# State
$ starchart state \
  --project-id=YOUR_PROJECT_ID \
  --package-path=PACKAGE_PATH

# Expose
$ starchart expose \
  --project-id=YOUR_PROJECT_ID \
  --package-path=PACKAGE_PATH

# Apply
$ starchart apply \
  --project-id=YOUR_PROJECT_ID \
  --package-path=PACKAGE_PATH
```

### model file

After you expose model by starchart, you get a model file like the following.
It define model and version information.

`MODEL_NAME.json`

```json
{
  "model": "MODEL_NAME",
  "versions": [
    {
      "version": {
        "name": "projects/PROJECT_ID/models/MODEL_NAME/versions/v20170111170842",
        "deploymentUri": "gs://PROJECT_ID-ml/MODEL_NAME/20170111170842/model",
        "createTime": "2017-01-11T09:12:54Z",
        "job": {
          "jobId": "MODEL_NAME_20170111170842",
          "trainingInput": {
            "packageUris": [
              "gs://PROJECT_ID-ml/MODEL_NAME/20170111170842/packages/trainer-0.0.0.tar.gz"
            ],
            "pythonModule": "trainer.task",
            "args": [
              "--model_dir=gs://PROJECT_ID-ml/MODEL_NAME/20170111170842/model",
              "--train_dir=gs://PROJECT_ID-ml/MODEL_NAME/20170111170842/train",
            ],
            "region": "us-central1"
          },
          "createTime": "2017-01-11T08:08:49Z",
          "startTime": "2017-01-11T08:13:55Z",
          "endTime": "2017-01-11T08:40:55Z",
          "state": "SUCCEEDED",
          "trainingOutput": {
            "consumedMLUnits": 0.45
          }
        },
        "isDefault": true
      }
    }
  ]
}
```

You can choose default version in this file (`isDefault`).

## TODO

- Add test option which test API input and output.

## Installation

```sh
$ pip install git+https://github.com/monochromegane/starchart.git
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/monochromegane/starchart.


## License

StarChart is licensed under the [MIT](http://opensource.org/licenses/MIT).

