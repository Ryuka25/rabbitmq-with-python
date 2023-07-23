FROM rabbitmq

RUN set eux; \
        rabbitmq-plugins enable --offline rabbitmq_management; \
# make sure the metrics collector is re-enabled (disabled in the base image for Prometheus-style metrics by default)
        rm -f /etc/rabbitmq/conf.d/20-management_agent.disable_metrics_collector.conf;

EXPOSE 15671 15672