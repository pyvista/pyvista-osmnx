def download_osmnx_graph(load=True):  # pragma: no cover
    """Load a simple street map from Open Street Map.

    Generated from:

    .. code:: python

        >>> import osmnx as ox  # doctest:+SKIP
        >>> address = 'Holzgerlingen DE'  # doctest:+SKIP
        >>> graph = ox.graph_from_address(
        ...     address, dist=500, network_type='drive'
        ... )  # doctest:+SKIP
        >>> pickle.dump(
        ...     graph, open('osmnx_graph.p', 'wb')
        ... )  # doctest:+SKIP

    Parameters
    ----------
    load : bool, default: True
        Load the dataset after downloading it when ``True``.  Set this
        to ``False`` and only the filename will be returned.

    Returns
    -------
    networkx.classes.multidigraph.MultiDiGraph
        An osmnx graph of the streets of Holzgerlingen, Germany.

    Examples
    --------
    >>> from pyvista import examples
    >>> graph = examples.download_osmnx_graph()  # doctest:+SKIP

    .. seealso::

        :ref:`Osmnx Graph Dataset <osmnx_graph_dataset>`
            See this dataset in the Dataset Gallery for more info.

        :ref:`open_street_map_example`
            Full example using this dataset.

    """
    try:
        import osmnx  # noqa: F401
    except ImportError:
        raise ImportError('Install `osmnx` to use this example')
    return _download_dataset(_dataset_osmnx_graph, load=load)


def _osmnx_graph_read_func(filename):  # pragma: no cover
    import pickle

    return pickle.load(Path(filename).open('rb'))  # noqa: SIM115


_dataset_osmnx_graph = _SingleFileDownloadableDatasetLoader(
    'osmnx_graph.p',
    read_func=_osmnx_graph_read_func,
)
