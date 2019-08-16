# Logging in Adaptive Cards

Adaptive Cards supports logging to various platforms, including telemetry platforms such as Microsoft 1DS.

## Logging API

A developer can log both messages and events to the platform(s) she specifies. The ACLogger API is as follows (method descriptions are available in IACLogger.ts):

```
	logWarn(message: string): void; 

	logError(message: string): void; 

	logVerbose(message: string): void; 

	logInfo(message: string): void; 
	
	logEvent(event: string, eventSourceName: string, correlationID?: string, valueSet?: object): void;

	configureCustomProviders(...providers: IACProvider[]): void;

	isTelemetryEnabled(): boolean;
```

## Enabling Logging

Telemetry is disabled by default. To enable this feature, uncomment the appropriate line in the `parse()` method of the `AdaptiveCard` class in `AdaptiveCards/source/nodejs/adaptivecards/card-elements.ts`. Providers must then be included in the parameters of the method call, e.g.:

`ACLogger.getOrCreate().configureCustomProviders(new ConsoleLogger(), new Microsoft1DSLogger());`

## Extensibility

The current logging architecture supports extension of both the base ACLogger as well as IACProviders. A ConsoleLogger and Microsoft1DSProvider is available with the base Adaptive Cards library.

### Extending ACLogger

Creating a new ACLogger requires implementing the IACLogger.ts interface and replacing all instantiations of the default logger in card-elements.ts to instantiations of the new logger implementation. While not required, it is recommended that any implementation of IACLogger retain the singleton pattern. This ensures the least amount of resources is used by the logger, and that the provider state is maintained.

### Extending ACProvider

New logging providers can be used by any class that implements the IACProvider interface. The new provider can be logged to by calling `configureCustomProviders()` and using the instantiated provider as a parameter before any logging calls.