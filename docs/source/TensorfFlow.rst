TensorFlow
==========

.. contents::
   :local:
   :depth: 2
   :backlinks: top

Introduction
------------
TensorFlow is an end‑to‑end open‑source platform for machine learning developed by Google Brain. It provides a comprehensive ecosystem of tools, libraries, and community resources that streamline every step of the ML workflow—from research prototyping to production deployment. Built with flexibility in mind, TensorFlow supports a wide range of use cases: you can train state‑of‑the‑art deep learning models, deploy them across heterogeneous environments, and optimize performance through hardware acceleration. Whether you’re a beginner exploring neural networks or an expert engineering distributed training pipelines, TensorFlow delivers the scalability, performance, and community support to power your ambitions.

History & Architecture
----------------------
Originally released in 2015, TensorFlow succeeded Google’s internal DistBelief system, emphasizing an open ecosystem and modular design. At its core, TensorFlow represents computations as dataflow graphs: **nodes** are operations (ops) and **edges** are multi‑dimensional arrays called **tensors**. This graph abstraction enables optimizations such as parallel execution, device placement, and graph pruning. Since TensorFlow 2.0, eager execution is the default, offering intuitive, imperative programming, while still allowing you to export static graphs via `tf.function` for high‑performance production workloads.

Key Features
------------
- **Eager Execution**  
  By default in TF 2.x, operations execute immediately, making debugging and development as natural as standard Python.

- **Keras Integration**  
  `tf.keras` provides a high‑level, user‑friendly API to build, train, and evaluate neural networks, backed by the power and flexibility of TensorFlow.

- **Distribution Strategies**  
  Seamlessly scale from a single GPU to multi‑GPU, multi‑machine, or TPU clusters using `tf.distribute.Strategy` classes like `MirroredStrategy` and `TPUStrategy`.

- **TensorBoard**  
  Visualize metrics, inspect graphs, profile performance, and compare experiments through an interactive web dashboard.

- **Robust Ecosystem**  
  Libraries such as **TensorFlow Data** (`tf.data`) for efficient data ingestion, **TensorFlow Hub** for reusable modules, **TensorFlow Lite** for on‑device inference, and **TensorFlow Extended (TFX)** for production pipelines.

- **Language & Platform Support**  
  Native APIs for Python, C++, JavaScript (TensorFlow.js), and Swift (TensorFlow Swift), along with mobile runtimes for Android and iOS.

Getting Started
---------------
Before diving into code, familiarize yourself with these high‑level steps:

1. **Install TensorFlow** on your development machine or server.  
2. **Prepare your data** with `tf.data` pipelines for performance and scalability.  
3. **Define a model** using `tf.keras` or custom `tf.Module` classes.  
4. **Train & evaluate** with built‑in optimizers, losses, and metrics.  
5. **Export** your model with `tf.saved_model` for serving or convert to TensorFlow Lite for mobile/embedded.  
6. **Monitor & debug** via TensorBoard and profiling tools.

Installation
------------
Install the latest stable release via PyPI:

.. code-block:: bash

   pip install tensorflow

For GPU support, ensure the correct CUDA and cuDNN versions are installed, then:

.. code-block:: bash

   pip install tensorflow‑gpu

See the official GPU guide at https://www.tensorflow.org/install/gpu for detailed compatibility matrices.

Quickstart Example
------------------
Let’s train a simple linear model in under 15 lines:

.. code-block:: python

   import tensorflow as tf

   # Prepare a simple dataset
   xs = tf.constant([1.0, 2.0, 3.0, 4.0])
   ys = tf.constant([0.0, -1.0, -2.0, -3.0])

   # Build a tf.keras model
   model = tf.keras.Sequential([
       tf.keras.layers.Dense(units=1, input_shape=[1])
   ])
   model.compile(optimizer='sgd', loss='mse')

   # Train
   model.fit(xs, ys, epochs=500, verbose=0)

   # Make a prediction
   print(model.predict([10.0]))  # ≈ -9.0

In this example:
- `tf.constant` creates immutable tensors.  
- `Sequential` defines a simple feed‑forward model.  
- `compile` sets the optimizer and loss.  
- `fit` runs the training loop.  
- `predict` performs inference on new data.

Core Concepts
-------------
Tensors
^^^^^^^
A **Tensor** is a generalization of vectors and matrices to potentially higher dimensions. It is the fundamental unit of data in TensorFlow.

Graphs & Execution Modes
^^^^^^^^^^^^^^^^^^^^^^^
- **Eager mode** executes operations immediately—great for debugging and interactive workflows.  
- **Graph mode** (via `@tf.function`) compiles Python functions into static graphs, enabling optimizations like kernel fusion and deployment portability.

Modules & Layers
^^^^^^^^^^^^^^^^
- **`tf.Module`**: Base class for stateful objects (e.g., custom layers, models).  
- **`tf.keras.layers`**: High‑level building blocks (Dense, Conv2D, LSTM, etc.).  
- **`tf.keras.Model`**: Encapsulates training, evaluation, and serialization logic.

Data Pipelines
--------------
Use `tf.data` to build performant, scalable input pipelines:

.. code-block:: python

   dataset = tf.data.Dataset.from_tensor_slices((features, labels))
   dataset = dataset.shuffle(buffer_size=1000).batch(32).prefetch(tf.data.AUTOTUNE)

Model Building with Keras
-------------------------
`tf.keras` combines ease-of-use with performance:

.. code-block:: python

   model = tf.keras.Sequential([
       tf.keras.layers.InputLayer(input_shape=(32, 32, 3)),
       tf.keras.layers.Conv2D(32, 3, activation='relu'),
       tf.keras.layers.MaxPooling2D(),
       tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(10, activation='softmax'),
   ])
   model.compile(
       optimizer='adam',
       loss='sparse_categorical_crossentropy',
       metrics=['accuracy']
   )
   model.summary()

Training & Evaluation
---------------------
- **Callbacks**: Extend training with `tf.keras.callbacks` (e.g., `EarlyStopping`, `ModelCheckpoint`).  
- **Metrics**: Use built‑in metrics (`Accuracy`, `Precision`) or define custom ones.  
- **Validation**: Supply `validation_data` to `model.fit` for real‑time evaluation.

Monitoring & Debugging
----------------------
TensorBoard integration is seamless:

.. code-block:: python

   tensorboard_cb = tf.keras.callbacks.TensorBoard(log_dir='logs/')
   model.fit(xs, ys, epochs=10, callbacks=[tensorboard_cb])

Launch TensorBoard:

.. code-block:: bash

   tensorboard --logdir=logs/

Deployment
----------
Export your model for serving:

.. code-block:: python

   tf.saved_model.save(model, 'exported_model/1')

Options for deployment:

- **TensorFlow Serving**: High-performance C++ serving system.  
- **TensorFlow Lite**: Optimize and convert models for mobile/embedded devices.  
- **TensorFlow.js**: Run models in the browser or on Node.js.  
- **TFX**: End‑to‑end platform for ML pipelines in production.

Ecosystem & Community
---------------------
TensorFlow boasts a vibrant community:

- **TensorFlow Hub**: Reusable pre‑trained modules.  
- **Model Garden**: State‑of‑the‑art models and research code.  
- **Community forums**: Stack Overflow, GitHub Issues, and TensorFlow Special Interest Groups.  

Chapters
--------
.. toctree::
   :maxdepth: 1
   :caption: 📖 Detailed Topics

   chapter01
   chapter02
   chapter03
   chapter04
   chapter05
   chapter06
   chapter07
   chapter08
   chapter09
   chapter10
