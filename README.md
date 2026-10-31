# Order Status Observers — Starter

## Your task
1. Introduce an `Observer` contract and subscription.
2. Adapt `CustomerNotifier` and `AuditObserver`.
3. Add `AnalyticsObserver` without changing `OrderStatus` notification logic.
4. Add/update one focused test.
5. Explain one lifecycle/coupling cost.


## Local setup

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Course conventions

- Python is only the implementation language for the exercise; the design roles are language-agnostic.
- Use an explicit object-oriented design.
- Keep one main class per source file.


## Design notes

| Role | Class |
| --- | --- |
| Observer (contract) | `Observer` |
| Subject | `Subject` |
| Concrete Subject | `OrderStatus` |
| Concrete Observers | `CustomerNotifier`, `AuditObserver`, `AnalyticsObserver` |

`OrderStatus` no longer knows any concrete receiver. It only calls `notify()` from `Subject`, which loops over whatever observers are subscribed. `CustomerNotifier` and `AuditObserver` keep their original methods and implement `update()` by delegating to them. `AnalyticsObserver` was added as a new class and subscribed from outside, without touching the notification logic.

Observers are attached with `subscribe()` and removed with `unsubscribe()`. Subscribing the same observer twice has no effect.

### Lifecycle / coupling cost

The subject keeps a strong reference to every subscribed observer. If an observer is not unsubscribed when it is no longer needed, it stays alive and keeps receiving updates (a lapsed listener / memory leak). The dependencies are also implicit: reading `OrderStatus` no longer tells you who reacts to a status change, that is decided wherever `subscribe()` is called, and the notification order depends on subscription order.
